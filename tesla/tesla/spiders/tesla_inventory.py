import scrapy


class TeslaInventorySpider(scrapy.Spider):
    name = 'tesla_inventory'
    allowed_domains = ['.']
    start_urls = ['http://./']

    def parse(self, response):
        pass
