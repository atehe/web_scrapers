import scrapy


class Covid19CaseSpider(scrapy.Spider):
    name = 'covid19_case'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['http://www.worldometers.info/']

    def parse(self, response):
        pass
