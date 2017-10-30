# -*- coding: utf-8 -*-
'''
    抓取上证E互动之沱牌舍得问答界面
'''
import scrapy
from homestead.items import SseinfoItem

class Sseinfo_shedeSpider(scrapy.Spider):
    name = 'Sseinfo_shede'
    allowed_domains = ['sns.sseinfo.com']
    start_urls = ['http://sns.sseinfo.com/company.do?uid=702']

    def parse(self,response):
        items = SseinfoItem()
        for sel in response.xpath('//div[@class="m_feed_item"]'):
            items['time'] = sel.xpath('div[@class="m_feed_detail m_qa"]/div[@class="m_feed_func top10"]/div[@class="m_feed_from"]/span/text()').extract()[0].strip()
            items['ask'] = sel.xpath('div[@class="m_feed_detail"]/div[@class="m_feed_cnt"]/div[@class="m_feed_txt"]/text()')[1].extract().strip()
            items['answer'] = sel.xpath('div[@class="m_feed_detail m_qa"]/div[@class="m_feed_cnt"]/div[@class="m_feed_txt"]/text()').extract()[0].strip()
            print(items['time'],'---=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=reade-=-=')
            yield items
