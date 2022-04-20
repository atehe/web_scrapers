import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector
import time


class HotelsSpider(scrapy.Spider):
    name = "hotels"
    allowed_domains = ["www.booking.com"]
    start_urls = [
        "https://www.booking.com/hotel/index.en-gb.html?aid=376363;label=bh-fm3txPOR2sVEAQeyBtYl_gS267777916216%3Apl%3Ata%3Ap1%3Ap22%2C563%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-1983705807%3Alp9076649%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YfqnDqqG8nt1XFzPnqOODws;sid=7cc1c3af8fec962eea2ba75b24a6c95c"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse_properties_listing)

    def parse_properties_listing(self, response):
        location = "United Kindgom"
        driver = response.request.meta["driver"]

        search_box = driver.find_element(by=By.XPATH, value="//input[@id='ss']")

        search_box.send_keys(location)
        search_box.send_keys(Keys.RETURN)

        time.sleep(5)

        page_response = Selector(text=driver.page_source)
        hotels_href = page_response.xpath('//div[@class="c90a25d457"]/a/@href').getall()
        print(hotels_href)
        for url in hotels_href:
            yield SeleniumRequest(
                url=url, callback=self.parse_hotel_page, meta={"Location": location}
            )

    def parse_hotel_page(self, response):

        yield {
            "Name": response.xpath("///h2[@id='hp_hotel_name']/text()[2]").get(),
            "Location": response.request.meta.get("Location"),
            "Address": response.xpath("//p[@id='showMap2']/span[1]/text()").get(),
            "Review Score": response.xpath(
                "//div[@data-testid='review-score-component']/div/text()"
            ).get(),
            "Scored By": response.xpath(
                "//div[@data-testid='review-score-component']/div[2]/span[2]/text()[2]"
            ).get(),
            "Popular Facilities": response.xpath(
                "(//div[@class='hp_desc_important_facilities clearfix hp_desc_important_facilities--bui '])[1]/div/text()[2]"
            ).getall(),
        }
