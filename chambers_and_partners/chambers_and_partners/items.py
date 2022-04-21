# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose


def absolute_url(rel_url):
    return f"www.chambers.com{rel_url}"


class ChambersAndPartnersItem(scrapy.Item):
    name = scrapy.Field(output_processor=TakeFirst())
    rank = scrapy.Field(output_processor=TakeFirst())
    law_firm = scrapy.Field(output_processor=TakeFirst())
    practice_area = scrapy.Field(output_processor=TakeFirst())
    location = scrapy.Field(output_processor=TakeFirst())
    region = scrapy.Field(output_processor=TakeFirst())
    profile_url = scrapy.Field(
        input_processor=MapCompose(absolute_url), output_processor=TakeFirst()
    )

    law_firm_url = scrapy.Field(
        input_processor=MapCompose(absolute_url), output_processor=TakeFirst()
    )
