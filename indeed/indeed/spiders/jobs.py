import scrapy
from urllib.parse import urlencode
from itemloaders import ItemLoader
from scrapy.utils.response import open_in_browser

# from indeed.items import IndeedItem


class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["https://ng.indeed.com"]
    query = {"q": "intern", "l": "lagos"}

    def start_requests(self):
        url = "https://ng.indeed.com/jobs?" + urlencode(self.query)
        yield scrapy.Request(url=url, callback=self.parse_job_listing)

    def parse_job_listing(self, response):
        open_in_browser(response)

        jobs_url = response.xpath(
            "//a[contains(@class,'resultWithShelf sponTapItem desktop')]/@href"
        ).getall()
        print(jobs_url)
        print(response.request.url)
        for url in jobs_url:
            abs_url = "https://ng.indeed.com" + url
            # yield response.follow(url=url, callback=self.parse_job_post)
            yield scrapy.Request(url=abs_url, callback=self.parse_job_post)

    def parse_job_post(self, response):
        loader = ItemLoader(item=IndeedItem(), selector=response)

        loader.add_xpath(
            "job_title", "//h1[contains(@class,'JobInfoHeader-title')]/text()"
        )
        loader.add_xpath(
            "company_name", "//div[@class='icl-u-lg-mr--sm icl-u-xs-mr--xs']/a/text()"
        )
        loader.add_xpath(
            "company_location", "//div[@id='salaryInfoAndJobType']/span/text()"
        )
        loader.add_xpath(
            "expected_salary", "//div[@id='salaryInfoAndJobType']/span/text()"
        )
        loader.add_xpath("job_description", "//div[@id='jobDescriptionText']//text()")
        loader.add_xpath("hiring", "//span[contains(text(), 'Hiring')]/b/text()")

        yield loader.load_item
