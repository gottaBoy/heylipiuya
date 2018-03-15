# -*- coding: utf-8 -*-
import scrapy
import time
import urllib2  
import random  
from dp3.items import Dp3Item

class Dianping3Spider(scrapy.Spider):
    name = 'dianping3'
    allowed_domains = ['dianping.com']
    start_urls = ['http://www.dianping.com/guangzhou/ch0']  #ch10-96  p1-p50 g101-g260  ch85/g182r1519
    
    #定义需要爬取的页面数量，以及爬取链接
    def start_requests(self) :
        reqs = []
        gid = [210,103,111,113,116,117,132,114,110,102,207,217,219,115,109,34055,508,34014,104,118,251,250,1959,34032,101,106,107,3243,1338,246,26481,2714,247,1783]
        rid = [24,26,25,22,1549,621,1963,1964,27,1555,1552,1554]
        qid = [243,236,95,259,354,307,355]
        #144 1964
        for i in gid: 
            for j in rid:
                # for k in qid: + 'q' + str(k)
                for m in range(1,51):
                    url = 'http://www.dianping.com/guangzhou/ch10/g' + str(i) +'r' + str(j)  +'p' + str(m)
                    req = scrapy.Request(url)
                    reqs.append(req)
        return reqs
        
    def parse(self, response) :
        item = Dp3Item()
        # 链接部分
        item['shop_url'] = response.xpath('//*[@id="shop-all-list"]/ul/li/div[1]/a/@href').extract()

        # item['shop_name'] = response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[1]/a/h4/text()').extract()
        # item['shop_city'] =  response.xpath('//*[@id="logo-input"]/div[1]/a[2]/span[2]/text()').extract()
        # item['shop_address_1'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[3]/a[2]/span/text()').extract()
        # item['shop_address_2'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[3]/span/text()').extract()
        # #shop_tel
        # # item['shop_star'] = (response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[2]/span/'))[0].attrib.get('title')
        # item['com_num'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[2]/a[1]/b/text()').extract()
        # item['price_avg'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[2]/a[2]/b/text()').extract()
        # item['tag_name'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[3]/a[1]/span/text()').extract()
        # item['kou_wei'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/span/span[1]/b/text()').extract()
        # item['huan_jing'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/span/span[2]/b/text()').extract()
        # item['fu_wu'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/span/span[3]/b/text()').extract()
        return item
