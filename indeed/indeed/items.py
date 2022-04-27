# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags


def clean_text(text):
    pass


class IndeedItem(scrapy.Item):
    job_title = scrapy.Field(
        input_processor=MapCompose(remove_tags), output_processor=TakeFirst()
    )
    company_name = scrapy.Field(
        input_processor=MapCompose(remove_tags), output_processor=TakeFirst()
    )
    company_location = scrapy.Field(
        input_processor=MapCompose(remove_tags), output_processor=TakeFirst()
    )
    expected_salary = scrapy.Field(
        input_processor=MapCompose(remove_tags), output_processor=TakeFirst()
    )
    job_description = scrapy.Field(
        input_processor=MapCompose(remove_tags), output_processor=Join()
    )
    hiring_number = scrapy.Field(
        input_processor=MapCompose(remove_tags), output_processor=TakeFirst()
    )
    time_posted = scrapy.Field(
        input_processor=MapCompose(remove_tags), output_processor=TakeFirst()
    )
    job_url = scrapy.Field()
