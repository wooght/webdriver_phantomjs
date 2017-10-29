# -*- coding: utf-8 -*-
import scrapy
from homestead.items import HomesteadItem

class XueqiuSpider(scrapy.Spider):
    name = 'xueqiu'
    allowed_domains = ['xueqiu.com']
    start_urls = ['http://xueqiu.com/']

    def parse(self, response):
        items = HomesteadItem()
        body = response.xpath("//body").extract()
        try:
            print('--------',body)
        except UnicodeEncodeError as e:
            print('Error:',e)
        items['body'] = body
        yield items
