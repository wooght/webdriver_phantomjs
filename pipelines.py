# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#引入依赖文件 DropItem
from scrapy.exceptions import DropItem
import json
from homestead.items import ArticleItem,HomesteadItem

class HomesteadPipeline(object):
    def open_spider(self,spider):
        pass
    def process_item(self, item, spider):                               #通过判断item类型来调用不同的pipeline来处理item
        if isinstance(item,ArticleItem):
            file = open('json/xueqiuarticle.json','a+',encoding='utf-8')
            line = json.dumps(dict(item),ensure_ascii=False)+"\n"
            file.write(line)
        elif isinstance(item,HomesteadItem):
            file = open('json/xueqiu.json','a+',encoding='utf-8')
            line = json.dumps(dict(item),ensure_ascii=False)+"\n"       #item是一个对象,要进行处理才能str格式保存
            file.write(line)
        return item

    def close_spider(self,spider):
        pass
