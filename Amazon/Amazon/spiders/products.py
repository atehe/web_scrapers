from gc import callbacks
import scrapy
from urllib.parse import urlencode
from itemloaders import ItemLoader
from Amazon.items import AmazonItem
from scrapy.utils.response import open_in_browser


class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["amazon.com"]
    search_queries = ["laptop"]
    page_num = 1

    def start_requests(self):
        for query in self.search_queries:
            url = "https://www.amazon.com/s?" + urlencode({"k": query})
            yield scrapy.Request(
                url=url,
                callback=self.parse_search_results,
                meta={"query": query},
                dont_filter=True,
            )

    def parse_search_results(self, response):
        products_url = response.xpath(
            "//div[@class='a-section']/div/div[2]/div/div/div/h2/a/@href"
        ).getall()
        for url in products_url:
            yield response.follow(url=url, callback=self.parse_product)

        next_page = response.xpath(
            "//a[contains(@class,'pagination') and contains(text(), 'Next')]/@href"
        ).get()

        if next_page:
            self.page_num += 1
            yield response.follow(url=next_page, callback=self.parse_search_results)

    def parse_product(self, response):
        loader = ItemLoader(item=AmazonItem(), selector=response)

        loader.add_xpath("Name", "//span[@id='productTitle']/text()")
        loader.add_xpath(
            "Rating",
            "//div[@id='averageCustomerReviews']/span/span/span/a/i/span/text()",
        )
        loader.add_xpath(
            "Number_of_reviews", "//span[@id='acrCustomerReviewText']/text()[1]"
        )
        loader.add_xpath(
            "Number_of_answered_questions", "//a[@id='askATFLink']/span/text()[1]"
        )
        loader.add_xpath(
            "Listing_price",
            "(//td[contains(text(),'Price')]/following-sibling::td/span/span[1]/text())[1]",
        )
        loader.add_xpath(
            "Discounted_price",
            "(//td[contains(text(),'Price')]/following-sibling::td/span/span[1]/text())[2]",
        )
        loader.add_xpath(
            "ASIN", "//th[contains(text(), 'ASIN')]/following-sibling::td/text()"
        )
        loader.add_xpath(
            "Product_Rank",
            "//th[contains(text(), 'Rank')]/following-sibling::td/span//text()",
        )
        loader.add_xpath(
            "Date_first_available",
            "//th[contains(text(), 'Date')]/following-sibling::td/text()",
        )

        yield loader.load_item()
