# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#引入依赖文件 DropItem
from scrapy.exceptions import DropItem
import json
from homestead.items import ArticleItem,HomesteadItem,SseinfoItem
import homestead.table as T

class HomesteadPipeline(object):
    def __init__(self):
        self.Article_file = open('json/xueqiuarticle.json','a+',encoding='utf-8')
        self.Homestead_file = open('json/xueqiu.json','a+',encoding='utf-8')
        self.Sseinfo_file = open('json/Sseinfo_shede.json','a+',encoding='utf-8')
    def open_spider(self,spider):
        print('spider open','-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    #spider没执行一次request得到response就会调用pipeline
    def process_item(self, item, spider):                               #通过判断item类型来调用不同的pipeline来处理item
        if isinstance(item,ArticleItem):
            line = json.dumps(dict(item),ensure_ascii=False)+"\n"
            self.Article_file.write(line)
        elif isinstance(item,HomesteadItem):
            line = json.dumps(dict(item),ensure_ascii=False)+"\n"       #item是一个对象,要进行处理才能str格式保存
            self.Homestead_file.write(line)
        elif isinstance(item,SseinfoItem):
            # line = json.dumps(dict(item),ensure_ascii=False)+"\n"
            # self.Sseinfo_file.write(line)
            i = T.sns_sseinfo.insert()
            r = T.conn.execute(i,dict(item))
        return None

    def close_spider(self,spider):
        pass
