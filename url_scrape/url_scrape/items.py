# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

def remove_whitespace(value):
    return value.strip()

class urlItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    input_processor = MapCompose(remove_tags, remove_whitespace),
    output_processor = TakeFirst()

# items from individual articles
class ArticleItems(scrapy.Item):
    article_title = scrapy.Field()
    article_date = scrapy.Field()
    article_body = scrapy.Field()
    image_link = scrapy.Field()
    category_1 = scrapy.Field()
    category_2 = scrapy.Field()
    category_3 = scrapy.Field()
    

