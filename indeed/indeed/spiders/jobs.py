import scrapy
from urllib.parse import urlencode
from itemloaders import ItemLoader
from scrapy.utils.response import open_in_browser
from indeed.items import IndeedItem


class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["ng.indeed.com"]
    query = {"q": "intern", "l": "lagos"}

    def start_requests(self):
        url = "https://ng.indeed.com/jobs?" + urlencode(self.query)

        yield scrapy.Request(url=url, callback=self.parse_job_listing)

    def parse_job_listing(self, response):
        jobs_url = (
            response.xpath(
                "//a[contains(@class,'resultWithShelf sponTapItem desktop')]/@href"
            ).getall()
            or response.xpath("//a[@class='jcs-JobTitle']/@href").getall()
        )
        for url in jobs_url:
            abs_url = "https://ng.indeed.com" + url
            yield response.follow(url=url, callback=self.parse_job_post)

        next_page = response.xpath(
            "//ul[@class='pagination-list']/li[position()=last()]/a/@href"
        ).get()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse_job_listing)

    def parse_job_post(self, response):
        loader = ItemLoader(item=IndeedItem(), selector=response)

        loader.add_xpath("job_title", "//h1[contains(@class,'JobInfoHeader-title')]")
        loader.add_xpath(
            "company_name", "//div[@class='icl-u-lg-mr--sm icl-u-xs-mr--xs']/a"
        )
        loader.add_xpath(
            "company_location",
            "//div[contains(@class,'jobsearch-InlineCompanyRating')]/following-sibling::div/div",
        )
        loader.add_xpath("expected_salary", "//div[@id='salaryInfoAndJobType']/span")
        loader.add_xpath("job_description", "//div[@id='jobDescriptionText']")

        loader.add_xpath(
            "hiring_number",
            "//span[contains(@class,'jobsearch-HiringInsights-icon jobsearch-HiringInsights-icon--multiplecandidates')]/following-sibling::span/b",
        )

        yield loader.load_item()
