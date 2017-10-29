# -*- coding: utf-8 -*-
import scrapy
from homestead.items import HomesteadItem

class XueqiuSpider(scrapy.Spider):
    name = 'xueqiu'
    allowed_domains = ['xueqiu.com']
    start_urls = ['http://xueqiu.com/']

    def parse(self, response):
        items = HomesteadItem()
        body = response.xpath("//body").extract()       #获取网页body内容
        try:
            print('--------',body)                      #打印会涉及到编码和当前显示问题
        except UnicodeEncodeError as e:
            print('Error:',e)
        items['body'] = body                            #只有Item类型才能传递给pipeline
        yield items
