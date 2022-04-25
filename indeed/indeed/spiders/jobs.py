import scrapy
from urllib.parse import urlencode
from itemloaders import ItemLoader
from indeed.items import IndeedItem

class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['']
    query = {'q':'intern','l':'lagos'}

    def start_requests(self):
        url = 'https://ng.indeed.com/jobs?' + urlencode(self.query)
        scrapy.Request(url=url, callback=self.parse)
    

    def parse_job_listing(self, response):
        jobs_url =  response.xpath("//a[contains(@class,'resultWithShelf sponTapItem desktop')]/@href").getall()
        
        for url in jobs_url:
            yield response.follow(url=url, callback=self.parse_job_post)
    
    def parse_job_post(self, response):
        loader = ItemLoader(item=IndeedItem(), selector=response)
        
        

        
    
