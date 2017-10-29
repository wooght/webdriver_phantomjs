# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'Demo'
    allowed_domains = ['demo']
    start_urls = ['http://demo/']

    def parse(self, response):
        pass
