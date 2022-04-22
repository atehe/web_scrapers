import scrapy
from urllib.parse import urlencode


search_queries = ["laptop", "camera"]


class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["amazon.com"]

    def start_request(self):
        for query in search_queries:
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
            yield response.follow(
                url=url,
                callback=self.parse_product,
                meta={"query": response.request.meta["query"]},
            )

    def parse_product(self, response):
        yield {
            "Name": response.xpath("//span[@id='productTitle']/@text()").get(),
            "Rating": response.xpath(
                "//div[@id='averageCustomerReviews']/span/span/span/a/i/span/text()[1]"
            ).get(),
            "Number of Reviews": response.xpath(
                "//span[@id='acrCustomerReviewText']/text()[1]"
            ).get(),
            "Number of Answered Question": response.xpath(
                "//a[@id='askATFLink']/span/text()[1]"
            ).get(),
            "Listing Price": response.xpath(
                "//div[@id='corePrice_desktop']/div/table/tbody/tr[1]/td[2]/span/span/text()"
            ).get(),
            "Current Price": response.xpath(
                "//div[@id='corePrice_desktop']/div/table/tbody/tr[2]/td[2]/span/span/text()"
            ).get(),
            "ASIN": response.xpath(
                "//th[contains(text(), 'ASIN')]/following-sibling::td/text()"
            ).get(),
            "Product Rank": response.xpath(
                "//th[contains(text(), 'Rank')]/following-sibling::td/span/span/text()"
            ).get(),
            "Date first Available": response.xpath(
                "//th[contains(text(), 'Date')]/following-sibling::td/text()"
            ).get(),
        }
