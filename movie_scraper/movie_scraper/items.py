# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Celebrity(scrapy.Item):
    name = scrapy.Field()
    highest_rated = scrapy.Field()
    lowest_rated = scrapy.Field()
    birthday = scrapy.Field()
    birthplace = scrapy.Field()

class MovieScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
