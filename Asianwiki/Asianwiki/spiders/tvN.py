import scrapy
from scrapy.utils.response import open_in_browser


class TvnSpider(scrapy.Spider):
    name = "tvN"
    allowed_domains = ["www.asianwiki.com"]
    start_urls = ["https://www.asianwiki.com/Category:TvN_Drama_Series"]

    def parse(self, response):
        open_in_browser(response)
