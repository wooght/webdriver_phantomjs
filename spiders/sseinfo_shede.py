# -*- coding: utf-8 -*-
'''
    抓取上证E互动之沱牌舍得问答界面
'''
import scrapy
import re
import time
from homestead.items import SseinfoItem

#以下两项 是spider拥有链接管理和追踪功能
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor

class Sseinfo_shedeSpider(CrawlSpider):
    name = 'Sseinfo_shede'
    allowed_domains = ['sns.sseinfo.com']
    start_urls = ['http://sns.sseinfo.com/']

    rules = (
        Rule(LinkExtractor(allow=('user.do\?uid=\d+',)),callback='parse_item',follow=False),
    )

    def parse_item(self,response):
        items = SseinfoItem()
        items['dm'] = response.xpath('//input[@id="company_txt"]/@value').extract()   #股票代码
        items['dm'] = self.sub_dm(items['dm'][0])
        for sel in response.xpath('//div[@class="m_feed_item"]'):
            # items['time'] = sel.xpath('div[@class="m_feed_detail m_qa"]/div[@class="m_feed_func top10"]/div[@class="m_feed_from"]/span/text()').extract()[0].strip()
            items['time'] = sel.xpath('div[@class="m_feed_detail m_qa"]//div[@class="m_feed_from"]/span/text()').extract()[0].strip()
            items['time'] = self.sub_time(items['time'])
            items['ask'] = sel.xpath('div[@class="m_feed_detail"]//div[@class="m_feed_txt"]/text()')[1].extract().strip()
            items['anwser'] = sel.xpath('div[@class="m_feed_detail m_qa"]/div[@class="m_feed_cnt"]/div[@class="m_feed_txt"]/text()').extract()[0].strip()
            print(items['dm'],'---=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=reade-=-=')
            yield items

    def sub_time(self,t):
        patten = re.compile(r'昨天')
        now = time.strftime("%m-%d",time.localtime())
        t = re.sub(patten,now,t)
        patten = re.compile(r'(\d+)月(\d+)日')
        return re.sub(patten,r'\1-\2',t)
    def sub_dm(self,dm):
        # 沱牌舍得(600702)
        return re.search(r'\((.*)\)',dm,re.I).group(1)

# xpath,css 参考 http://blog.csdn.net/ahri_j/article/details/72196823
