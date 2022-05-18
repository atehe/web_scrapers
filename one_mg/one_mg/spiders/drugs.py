import scrapy
from scrapy_selenium import SeleniumRequest
from scrapy.utils.response import open_in_browser


class DrugsSpider(scrapy.Spider):
    name = "drugs"
    allowed_domains = ["1mg.com"]

    def start_requests(self):
        index_letters = "a"
        for letter in index_letters:
            url = f"https://www.1mg.com/drugs-all-medicines?label={letter}"
            yield SeleniumRequest(url=url, callback=self.parse, wait_time=10)
            # yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        open_in_browser(response)
        products = response.xpath("//div[contains(@class, '__product-grid__')]")

        for product in products:
            yield {
                "name": product.xpath(".//a/div[2]/div[1]/div[1]/text()").get(),
                "price": "".join(
                    product.xpath(".//a/div[2]/div[1]/div[2]/text()").getall()
                ),
                "prescription": product.xpath(".//a/div[2]/div[3]/div[1]/text()").get(),
                "manufacturer": product.xpath(".//a/div[2]/div[3]/div[2]/text()").get(),
                "salt composition": product.xpath(
                    ".//a/div[2]/div[4]/div[1]/text()"
                ).get(),
                "product_url": product.xpath(".//a/@href").get(),
            }

        # last_page = response.xpath(
        #     "//ul[@class='list-pagination']/li[position()=(last()-1)]/a/text()"
        # ).get()

        # for page_num in range(2, int(last_page)):
        #     url = response.url + f"&page={page_num}"
        #     yield SeleniumRequest(url=url, callback=self.parse, wait_time=5)
