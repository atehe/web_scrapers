import scrapy


class TvnSpider(scrapy.Spider):
    name = 'tvN'
    allowed_domains = ['www.asianwiki.com']
    start_urls = ['http://www.asianwiki.com/']

    def parse(self, response):
        pass
