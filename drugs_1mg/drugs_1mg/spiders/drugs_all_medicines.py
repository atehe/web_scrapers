from gc import callbacks
import scrapy
from scrapy.utils.response import open_in_browser
from scrapy_selenium import SeleniumRequest


class DrugsAllMedicinesSpider(scrapy.Spider):
    name = "drugs_all_medicines"
    allowed_domains = ["www.1mg.com"]

    def start_requests(self):
        index_letters = "l"
        for letter in index_letters:
            url = f"https://www.1mg.com/drugs-all-medicines?label={letter}"
            yield SeleniumRequest(url=url, callback=self.parse, wait_time=5)

    def parse(self, response):

        products_url = response.xpath(
            "//div[contains(@class, '__product-grid__')]//a/@href"
        ).getall()
        print(products_url)

        for url in products_url:
            url = response.urljoin(url)
            # url = f"https://www.1mg.com{url}"
            yield SeleniumRequest(url=url, callback=self.parse_drug, wait_time=5)

        # for product in products:
        #     yield {
        #         "product_url": product.xpath(".//a/@href").get(),
        #         "name": product.xpath(".//a/div[2]/div[1]/div[1]/text()").get(),
        #         "price": "".join(
        #             product.xpath(".//a/div[2]/div[1]/div[2]/text()").getall()
        #         ),
        #         "prescription": product.xpath(".//a/div[2]/div[3]/div[1]/text()").get(),
        #         "manufacturer": product.xpath(".//a/div[2]/div[3]/div[2]/text()").get(),
        #         "salt composition": product.xpath(
        #             ".//a/div[2]/div[4]/div[1]/text()"
        #         ).get(),
        #     }

        # last_page = response.xpath(
        #     "//ul[@class='list-pagination']/li[position()=(last()-1)]/a/text()"
        # ).get()
        # for page_num in range(2, int(last_page)):
        #     url = response.url + f"&page={page_num}"
        #     yield SeleniumRequest(url=url, callback=self.parse, wait_time=10)

    def parse_drug(self, response):
        # open_in_browser(response)
        print("hellos")
        print(response.request.url)
