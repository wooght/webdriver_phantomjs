# -*- coding: utf-8 -*-
'''
    Rule,LinkExtractor
    实现连接管理
'''
import scrapy
from homestead.items import HomesteadItem
from homestead.items import ArticleItem
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
import re

class Xueqiu2Spider(CrawlSpider):
    name = 'xueqiu2'
    allowed_domains = ['xueqiu.com']
    start_urls = ['http://xueqiu.com/']

    #连接控制 LinkExtractor 连接提取器
    rules = (
        Rule(LinkExtractor(allow=('\/\d+\/\d+',)),callback='parse_item',follow=True),           #allow可以是具体连接,也可以是正则表达式
    )

    #CrawlSpider类已经重写了parse方法,在spider中不需要在写方法.
    
    #如果start_url解析和rules里面的解析方法不同 start_url就采用parse_start_url来解析
    def parse_start_url(self, response):
        items = HomesteadItem()
        body = response.xpath("//body").extract()       #获取网页body内容
        # try:
        #     print('--------',body)                      #打印会涉及到编码和当前显示问题
        # except UnicodeEncodeError as e:
        #     print('--------------Error---------------:',e)
        items['body'] = body                            #只有Item类型才能传递给pipeline
        yield items
        # for url in self.start_urls :
        #     yield self.make_requests_from_url(url)

    def parse_item(self,response):
        print(response.url,'------------------------------------------------访问')
        items = ArticleItem()
        # self.log('this is an item url:%s' % response.url,'\n')
        items['title'] = response.xpath('//title/text()').extract()
        items['thetime'] = response.xpath('//a[@class="time"]/text()').extract()
        items['src'] = str(response.url)
        items['article'] = response.xpath('//body').extract()
        yield items
