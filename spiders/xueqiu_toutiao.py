# -*- coding: utf-8 -*-
'''
    雪球头条内容抓取
'''
import scrapy
from homestead.items import HomesteadItem
from homestead.items import ArticleItem,XueqiutoutiaoItem
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor

from scrapy.exceptions import CloseSpider
import re

class Xueqiu2Spider(CrawlSpider):
    name = 'Xueqiutoutiao'
    allowed_domains = ['xueqiu.com']
    start_urls = ['https://xueqiu.com']

    run_num=0
    run_limit = 10000

    #连接控制 LinkExtractor 连接提取器
    rules = (
        Rule(LinkExtractor(allow=('\/\d+\/\d+',)),callback='parse_item',follow=True),           #allow可以是具体连接,也可以是正则表达式 follow指是否需要在该连接下跟进
        Rule(LinkExtractor(allow=('\/\d+\/column',)),callback='parse',follow=True),             #callback 指向默认 则当首页使用
    )

    #处理首页
    # def parse_start_url(self, response):
        # /7024454928/column
        # items = HomesteadItem()
        # body = response.xpath('//div[@class="article__widget"]/a/@href').extract()       #获取网页body内容
        # if(len(body)):
        #     print(body)
        #     url = response.urljoin(body[0])
        #     yield scrapy.Request(url)
        # #yield items
        # # yield scrapy.Request(url) 可以对url进行管理后再交给rules管理


    #处理Rule匹配成功的页面
    def parse_item(self,response):
        if(self.run_num<self.run_limit):
            self.run_num+=1
            items = XueqiutoutiaoItem()
            items['title'] = response.xpath('//title/text()').extract()[0].strip()
            # items['title'] = response.meta['web_title']
            items['time'] = response.xpath('//a[@class="time"]/text()').extract()[0].strip()
            url_re = re.search(r'.*\/(\d+)\/(\d+)$',response.url,re.I)
            items['url'] = url_re.group(1)+url_re.group(2)
            items['body'] = response.xpath('//div[@class="article__bd__detail"]').extract()[0].strip()
            print(items['title'])
            yield items
        else:
            raise  CloseSpider('close it')
