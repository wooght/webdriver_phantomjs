# -*- coding: utf-8 -*-

#通过python脚本启动scrapy

from scrapy.cmdline import execute
import threading
from threading import Timer

thread=[]       #线程池

#scrapy 运行接口
def scrapyrun(args):
    execute(["scrapy", "crawl", args])

#开启线程操作
class ThreadClass(threading.Thread):
    #重写构造函数,可以添加参数以便传递给线程主体调用
    def __init__(self,args):
        super(ThreadClass,self).__init__()      #调用父类构造函数
        self.args = args

    def run(self):
        scrapyrun(self.args)

spiders = ['Xueqiutoutiao']

# if __name__=='__main__':
#     for item in spiders:
#         #注册一个线程
#         thread.append(ThreadClass(item))
#         #开始线程
#         thread[-1].start()
for item in spiders:
    scrapyrun(item)
