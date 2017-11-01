# -*- coding: utf-8 -*-
'''
    上证E互动之问答
    第一财经只股票
'''
import scrapy
import re
import time
from homestead.items import SseinfoItem,YicaiItem

#以下两项 是spider拥有链接管理和追踪功能
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor

class Sseinfo_shedeSpider(CrawlSpider):
    name = 'Sseinfo_shede'
    allowed_domains = ['sns.sseinfo.com','www.yicai.com']
    start_urls = ['http://sns.sseinfo.com/',                #上证E互动
                'http://www.yicai.com/news/gushi/']         #第一财经只股票新闻

    rules = (
        Rule(LinkExtractor(allow=('user.do\?uid=\d+',)),callback='parse_sseinfo',follow=False),
        Rule(LinkExtractor(allow=('http\:\/\/www\.yicai\.com\/news\/\d+\.html',)),callback='parse_yicai',follow=False)
    )

    def parse_start_url(self,response):
        pass

    #E 互动
    def parse_sseinfo(self,response):
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

    #第一财经
    def parse_yicai(self,response):
        items = YicaiItem()
        items['title'] = response.xpath('//head/title/text()').extract()[0].strip()
        items['time'] = response.xpath('//div[@class="m-title f-pr"]/h2//span[2]/text()').extract()[0].strip()
        h_num = re.search(r'\/(\d+)\.html',response.url,re.I).group(1)
        items['url'] = h_num
        items['body'] = response.xpath('//div[@class="m-text"]').extract()[0].strip().encode('utf-8')
        print(h_num,'=-=-=-=-=-=-=-=-=-=-=-=-=yicai reade-=-=-=-=-=-')
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
