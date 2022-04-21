import scrapy
from scrapy.utils.response import open_in_browser
import cfscrape


class TvnSpider(scrapy.Spider):
    name = "tvN"
    allowed_domains = ["www.asianwiki.com"]
    start_urls = ["https://www.asianwiki.com/Category:TvN_Drama_Series"]

    def start_requests(self):
        for url in self.start_urls:
            token, agent = cfscrape.get_tokens(
                url,
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
            )
            yield scrapy.Request(
                url=url,
                cookies=token,
                headers={"User-Agent": agent},
                callback=self.parse,
            )

    def parse(self, response):
        open_in_browser(response)
