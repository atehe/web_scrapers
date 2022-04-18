import scrapy


class LawyersSpider(scrapy.Spider):
    name = 'lawyers'
    allowed_domains = ['chambers.com']
    start_urls = ['http://chambers.com/']

    def parse(self, response):
        pass
