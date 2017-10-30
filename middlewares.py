# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from selenium import webdriver
import time
# from scrapy.downloadermiddlewares.stats import DownloaderStats
from scrapy.http import Request, FormRequest, HtmlResponse

#headers
cap = webdriver.DesiredCapabilities.PHANTOMJS
cap["phantomjs.page.settings.resourceTimeout"] = 1000
cap["phantomjs.page.settings.loadImages"] = False
cap["phantomjs.page.settings.disk-cache"] = True
cap["phantomjs.page.customHeaders.Cookie"] = 'aliyungf_tc=AQAAAIplnShTMAQAebbT3lEVm4rc3txx; '
cap["phantomjs.page.settings.userAgent"] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
cap['phantomjs.page.settings.connection'] = 'keep-alive'
cap['phantomjs.page.settings.host'] = 'xueqiu.com'


#定义在外部 防止多次实例phantomjs
global  driver
#service_args=['..'] 具备访问加密请求https的功能
driver = webdriver.PhantomJS(service_args=['--ssl-protocol=any'],executable_path="F:\homestead/phantomjs",desired_capabilities=cap)

class WooghtDownloadMiddleware(object):

    def process_request(self, request, spider):
        global driver
        js = "var q=document.body.scrollTop=3000"
        url=request.url;
        if(spider.name=='xueqiu2'):                                                         #特定spider允许
            #雪球首页
            driver.get(url)
            time.sleep(2)
            driver.execute_script(js)                                                       #运行JS 模拟滑动到底部
            time.sleep(2)
            driver.execute_script("var a=document.body.scrollTop=5000")                     #第二次下拉
            print('delay 2S----------------------------------------------------\n')
            body = driver.page_source                                                       #获取素有内容
            print("\n---------------------3-----访问-----3------"+request.url,'\n')
            # driver.quit()                                                                 #关闭浏览器,只能关闭一次 如果每次调用都关闭,会遭到反爬虫
            response = HtmlResponse(body=body, encoding='utf-8',request=request,url=str(url))   #返回response数据供spider paser处理
            response.meta['web_title'] = driver.title                                       #传递其他参数供spider使用
            return response
        elif(spider.name=='Sseinfo_shede'):
            #上证E互动-沱牌舍得问答
            driver.get(url)
            time.sleep(2)
            driver.execute_script(js)
            time.sleep(1)
            print("\n---------------------4-----访问-----4------"+url,'\n')
            driver.execute_script("var a=document.body.scrollTop=5000")
            time.sleep(2)
            driver.execute_script("var b=document.body.scrollTop=8000")
            time.sleep(1)
            driver.execute_script("var b=document.body.scrollTop=10000")
            body = driver.page_source
            print(driver.title,'访问到了---=-=-=-=-=-=-=-=-=-')
            return HtmlResponse(body=body, encoding='utf-8',request=request,url=str(url))


#
# class HomesteadSpiderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_spider_input(self, response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.
#
#         # Should return None or raise an exception.
#         return None
#
#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.
#
#         # Must return an iterable of Request, dict or Item objects.
#         for i in result:
#             yield i
#
#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.
#
#         # Should return either None or an iterable of Response, dict
#         # or Item objects.
#         pass
#
#     def process_start_requests(self, start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.
#
#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
