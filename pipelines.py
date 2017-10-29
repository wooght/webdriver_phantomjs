# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import json

class HomesteadPipeline(object):
    def process_item(self, item, spider):
        file = open('json/xueqiu.json','w',encoding='utf-8')
        line = json.dumps(dict(item),ensure_ascii=False)+"\n"
        file.write(line)
        return item
