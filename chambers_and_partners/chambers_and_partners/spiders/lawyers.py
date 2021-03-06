import scrapy
from itemloaders import ItemLoader
from chambers_and_partners.items import ChambersAndPartnersItem
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from scrapy_selenium import SeleniumRequest
from scrapy.selector import Selector
import logging
import time


class LawyersSpider(scrapy.Spider):
    name = "lawyers"
    allowed_domains = ["chambers.com"]
    start_urls = [
        "https://chambers.com/legal-guide/gc-influencers-77",
    ]

    @staticmethod
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

        values = driver.find_elements(
            by=By.XPATH,
            value="//div[@class='list-item-container']/cmb-infinite-scroll/div/div",
        )

        if len(values) < 2:
            action.click()
            action.perform()
            return "no value"

        value = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@scrollid='{value_id}']"))
        )
        selected_value = value.text

        # logging
        if drop_down_id == 1:
            logging.info(f"Getting Region/Guide {selected_value}...")
        elif drop_down_id == 2:
            logging.info(f"Getting Location {selected_value}...")
        elif drop_down_id == 3:
            logging.info(f"Getting Practice {selected_value}...")

        last_value = driver.find_element(
            by=By.XPATH, value="//div[@class='item d-block'][position()=last()]"
        ).get_attribute("scrollid")

        if value_id != int(last_value):
            value.click()
            return selected_value, False

        else:
            value.click()
            return selected_value, True

    @staticmethod
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
        time.sleep(3)  # wait for page to load

    @staticmethod
    def go_to_tab(tab, driver):
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        f"//li[@class='nav-item']/span[contains(text(), '{tab}')]",
                    )
                )
            ).click()
            time.sleep(1)
        except:
            logging.info(f"Only {tab} available")

    @staticmethod
    def handle_cookies(driver):
        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
                )
            ).click()
            logging.info("Cookies Accepted")
        except:
            logging.info("No Cookies popup detected")

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        REGION_DROP_DOWN_ID = 1
        LOCATION_DROP_DOWN_ID = 2
        PRACTICE_AREA_DROP_DOWN_ID = 3

        driver = response.request.meta["driver"]
        driver.maximize_window()  # page format changes in small windows

        self.handle_cookies(driver)
        time.sleep(2)

        regions_to_scrape = (1, 2)
        for region_id in regions_to_scrape:
            region = self.drop_n_click(REGION_DROP_DOWN_ID, region_id, driver)
            time.sleep(2)  # wait for drop down to be populated

            location_id = 0
            while True:
                try:
                    location = self.drop_n_click(
                        LOCATION_DROP_DOWN_ID, location_id, driver
                    )
                    time.sleep(2)  # wait for drop down to be populated
                except:
                    logging.error(
                        f"Could not scrape Location with scroll id: {location_id}"
                    )
                    location_id += 1
                    continue

                practice_area_id = 0
                while True:
                    try:
                        practice_area = self.drop_n_click(
                            PRACTICE_AREA_DROP_DOWN_ID, practice_area_id, driver
                        )
                        if practice_area == "no value":
                            break
                        self.click_search(driver)
                        self.go_to_tab("Ranked Lawyers", driver)
                    except:
                        logging.error(
                            f"Could not scrape Practice in {region}, {location} with scroll id: {location_id}"
                        )
                        practice_area_id += 1
                        continue

                    page_response = Selector(text=driver.page_source.encode("utf-8"))
                    rankings = page_response.xpath(
                        "//app-rankings-tabs/div[1]/div/div/div"
                    )

                    logging.info("Scraping Page...")
                    for ranking in rankings:
                        rank = ranking.xpath("./h4/text()").get()
                        lawyers = ranking.xpath("./div[p]")

                        for lawyer in lawyers:
                            loader = ItemLoader(
                                item=ChambersAndPartnersItem(), selector=lawyer
                            )
                            loader.add_xpath("name", "./p[1]/a/text()")
                            loader.add_value("rank", rank)
                            loader.add_xpath("law_firm", "./p[2]/a/i/text()")
                            loader.add_value("practice_area", practice_area[0])
                            loader.add_value("location", location[0])
                            loader.add_value("region", region[0])
                            loader.add_xpath("profile_url", "./p[1]/a/@href")
                            loader.add_xpath("law_firm_url", "./p[2]/a/@href")

                            yield loader.load_item()

                    practice_area_id += 1
                    if practice_area[1]:
                        break
                    continue

                location_id += 1
                if location[1]:
                    break
                continue
