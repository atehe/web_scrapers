# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from typing import Type
import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Join


def clean_newline(data):
    return data.strip("\n").strip()


def format_numbers(num):
    num = "".join(num.split(","))
    return num.strip("#")


class MyanimelistItem(scrapy.Item):
    Title = scrapy.Field(
        input_processor=MapCompose(clean_newline), output_processor=TakeFirst()
    )
    Alternative_Titles = scrapy.Field(
        input_processor=MapCompose(clean_newline), output_processor=TakeFirst()
    )
    Type = scrapy.Field(
        input_processor=MapCompose(clean_newline), output_processor=TakeFirst()
    )
    Episodes = scrapy.Field(
        input_processor=MapCompose(clean_newline, format_numbers),
        output_processor=TakeFirst(),
    )
    Status = scrapy.Field(
        input_processor=MapCompose(clean_newline), output_processor=TakeFirst()
    )
    Aired = scrapy.Field(
        input_processor=MapCompose(clean_newline), output_processor=TakeFirst()
    )
    Premiered = scrapy.Field(
        input_processor=MapCompose(clean_newline), output_processor=TakeFirst()
    )
    Broadcast = scrapy.Field(
        input_processor=MapCompose(clean_newline), output_processor=TakeFirst()
    )
    Producers = scrapy.Field(
        input_processor=MapCompose(clean_newline), output_processor=Join(", ")
    )
    Licensors = scrapy.Field(
        input_processor=MapCompose(clean_newline), output_processor=Join(", ")
    )
    Studio = scrapy.Field(
        input_processor=MapCompose(clean_newline), output_processor=Join(", ")
    )
    Source = scrapy.Field(
        input_processor=MapCompose(clean_newline), output_processor=TakeFirst()
    )
    Genre = scrapy.Field(
        input_processor=MapCompose(clean_newline), output_processor=TakeFirst()
    )
    Theme = scrapy.Field(
        input_processor=MapCompose(clean_newline), output_processor=Join(", ")
    )
    Demographic = scrapy.Field(
        input_processor=MapCompose(clean_newline), output_processor=TakeFirst()
    )
    Duration = scrapy.Field(
        input_processor=MapCompose(clean_newline), output_processor=TakeFirst()
    )
    Rating = scrapy.Field(
        input_processor=MapCompose(clean_newline), output_processor=TakeFirst()
    )
    Score = scrapy.Field(
        input_processor=MapCompose(clean_newline), output_processor=TakeFirst()
    )
    Scored_By = scrapy.Field(
        input_processor=MapCompose(clean_newline, format_numbers),
        output_processor=TakeFirst(),
    )
    Ranked = scrapy.Field(
        input_processor=MapCompose(clean_newline, format_numbers),
        output_processor=TakeFirst(),
    )
    Popularity = scrapy.Field(
        input_processor=MapCompose(clean_newline, format_numbers),
        output_processor=TakeFirst(),
    )
    Members = scrapy.Field(
        input_processor=MapCompose(clean_newline, format_numbers),
        output_processor=TakeFirst(),
    )
    Favorites = scrapy.Field(
        input_processor=MapCompose(clean_newline, format_numbers),
        output_processor=TakeFirst(),
    )
