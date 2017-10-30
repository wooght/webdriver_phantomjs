# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HomesteadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    body = scrapy.Field()

class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    article = scrapy.Field()
    thetime = scrapy.Field()
    src = scrapy.Field()

class SseinfoItem(scrapy.Item):
    ask = scrapy.Field()
    time = scrapy.Field()
    answer = scrapy.Field()
