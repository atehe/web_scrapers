# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IndeedItem(scrapy.Item):
    job_title = scrapy.Field()
    company_name = scrapy.Field()
    company_location = scrapy.Field()
    expected_salary = scrapy.Field()
    job_description = scrapy.Field()
    hiring_number = scrapy.Field()
