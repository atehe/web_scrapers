# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, Join, MapCompose
from w3lib.html import strip_html5_whitespace


def strip_stars(col):
    return col.strip("out of 5 stars")


def strip_ratings(col):
    return col.strip("ratings")


def strip_answererd_question(col):
    return col.strip("answered questions")


def format_discounted_price(price):
    if not price:
        return None
    else:
        return price


class AmazonItem(scrapy.Item):
    Name = scrapy.Field(
        input_processor=(MapCompose(strip_html5_whitespace)),
        output_processor=TakeFirst(),
    )
    Rating = scrapy.Field(
        input_processor=(MapCompose(strip_html5_whitespace, strip_stars)),
        output_processor=TakeFirst(),
    )
    Number_of_reviews = scrapy.Field(
        input_processor=(MapCompose(strip_html5_whitespace, strip_ratings)),
        output_processor=TakeFirst(),
    )
    Number_of_answered_questions = scrapy.Field(
        input_processor=(MapCompose(strip_html5_whitespace, strip_answererd_question)),
        output_processor=TakeFirst(),
    )
    Listing_price = scrapy.Field(
        input_processor=(MapCompose(strip_html5_whitespace)),
        output_processor=TakeFirst(),
    )
    Discounted_price = scrapy.Field(
        input_processor=(MapCompose(strip_html5_whitespace, format_discounted_price)),
        output_processor=TakeFirst(),
    )
    ASIN = scrapy.Field(
        input_processor=(MapCompose(strip_html5_whitespace)),
        output_processor=TakeFirst(),
    )
    Product_Rank = scrapy.Field(output_processor=Join())
    Date_first_available = scrapy.Field(
        input_processor=(MapCompose(strip_html5_whitespace)),
        output_processor=TakeFirst(),
    )
