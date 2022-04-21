import scrapy
from quote_scraper.items import QuoteScraperItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']")
        for quote in quotes:
            item = QuoteScraperItem()
            item["text"] = quote.xpath(".//span[1]/text()").get()
            item["author"] = quote.xpath(".//span[2]/small/text()").get()
            item["tags"] = quote.xpath(".//div/a[@class='tag']/text()").getall()
            yield item

        next_page = response.xpath("//li[@class='next']/a/@href").get()
        page_num = int(next_page[-2])

        if next_page and page_num <= 5:
            yield response.follow(url=next_page, callback=self.parse)
