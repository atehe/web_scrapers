import scrapy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from scrapy_selenium import SeleniumRequest
from scrapy.selector import Selector
import logging

# import bs4
import time


def drop_n_click(drop_down_id, value_id, driver):
    drop_down = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"(//button[@class='btn btn-primary toggle-button'])[{drop_down_id}]",
            )
        )
    )
    action = ActionChains(driver)
    action.move_to_element(to_element=drop_down)
    action.click()
    action.perform()

    value = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//div[@scrollid='{value_id}']"))
    )
    if drop_down_id == 1:
        logging.info(f"Getting Region {value.text}...")
    elif drop_down_id == 2:
        logging.info(f"Getting Location {value.text}...")
    elif drop_down_id == 3:
        logging.info(f"Getting Practice {value.text}...")

    # checks for last value in dropdown (anchor doesn't have nested div)
    try:
        driver.find_element(
            by=By.XPATH,
            value=f"//div[@scrollid='{value_id}']/following-sibling::div/div",
        )
        value.click()

    except:
        value.click()
        return True


def click_search(driver):
    search = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[@class='btn btn-chambers-light-blue mt-1 w-100']",
            )
        )
    )
    action = ActionChains(driver)
    action.move_to_element(to_element=search)
    action.click()
    action.perform()


def go_to_tab(tab, driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                f"//li[@class='nav-item']/span[contains(text(), '{tab}')]",
            )
        )
    ).click()


class LawyersSpider(scrapy.Spider):
    name = "lawyers"
    allowed_domains = ["chambers.com"]
    start_urls = ["https://chambers.com/legal-guide/usa-5"]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
            )

    def parse(self, response):

        LOCATION_DROP_DOWN = 2  # location dropdown identifier
        PRACTICE_AREA_DROP_DOWN = 3  # practice area dropdown identifier
        LOCATIONS = 81  # number of locations in dropdown

        driver = response.request.meta["driver"]

        # Accepts cookies if popped up
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
                )
            ).click()
            logging.info("Cookies Accepted")
        finally:
            # driver.implicitly_wait(10)
            time.sleep(5)

        for location_id in range(LOCATIONS):
            try:
                drop_n_click(LOCATION_DROP_DOWN, location_id, driver)
                # driver.implicitly_wait(10)
                time.sleep(5)

                practice_area_id = 0
                while True:
                    last_item = drop_n_click(
                        PRACTICE_AREA_DROP_DOWN, practice_area_id, driver
                    )
                    click_search(driver)
                    go_to_tab("Ranked Lawyers", driver)
                    practice_area_id += 1

                    page_response = Selector(driver.page_source)
                    rankings = page_response.xpath(
                        "//app-rankings-tabs/div[1]/div/div/div"
                    )

                    for ranking in rankings:
                        rank = ranking.xpath("./h4/text()").get()
                        lawyers = ranking.xpath("./div[p]")

                        for lawyer in lawyers:
                            yield {
                                "Name": lawyer.xpath("./p[1]/a/text()").get(),
                                "Profile URL": "www.chambers.com"
                                + lawyer.xpath("./p[1]/a/@href").get(),
                                "Law Firm": lawyer.xpath("./p[2]/a/text()").get(),
                                "Law Firm URL": "www.chambers.com"
                                + lawyer.xpath("./p[2]/a/@href").get(),
                                "Rank": rank,
                            }

                    if last_item:
                        break
                    continue

                    # logging.info("Scraping")

            except:
                logging.error(
                    f"Could not scrape location with scroll id: {location_id}"
                )
                continue
