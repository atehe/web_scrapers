import scrapy
from scrapy.utils.response import open_in_browser


class DrugsAllMedicinesSpider(scrapy.Spider):
    name = "drugs_all_medicines"
    allowed_domains = ["www.1mg.com"]

    def start_requests(self):
        index_letters = "abcdefghijklmnopqrstuvwstqrstuvwxyz"
        for letter in index_letters:
            url = f"https://www.1mg.com/drugs-all-medicines?label={letter}"
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        open_in_browser(response)

        products = response.xpath("//div[contains(@class, '__product-grid__')]/div")
        for product in products:
            yield {
                "product_url": product.xpath(".//a/@href").get(),
                "name": product.xpath(".//a/div[2]/div[1]/div[1]/text()").get(),
                "price": "".join(
                    product.xpath(".//a/div[2]/div[1]/div[2]/text()").getall()
                ),
                "prescription": product.xpath(".//a/div[2]/div[3]/div[1]/text()").get(),
                "manufacturer": product.xpath(".//a/div[2]/div[3]/div[2]/text()").get(),
                "salt composition": product.xpath(
                    ".//a/div[2]/div[4]/div[1]/text()"
                ).get(),
            }
