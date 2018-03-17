# -*- coding: utf-8 -*-
import scrapy
import time
import urllib2  
import random  
from dp2.items import Dp2Item
# http://snipplr.com/all/tags/scrapy/
# http://www.meijutt.com/new100.html
# https://www.jianshu.com/
# https://movie.douban.com/cinema/nowplaying/hangzhou/
# https://api.douban.com/v2/book/2129650
# http://quotes.toscrape.com/page/1/
# https://www.dianping.com/search/keyword/2086/0_111
# http://www.dianping.com/guangzhou/ch10/g101
# http://www.dianping.com/ajax/citylist/getAllDomesticCity
# scrapy crawl dianping -o dianping.csv
class DianpingSpider(scrapy.Spider):
    name = 'dianping'
    allowed_domains = ['dianping.com']
    start_urls = ['http://www.dianping.com/guangzhou/ch0']  #ch10-96  p1-p50 g101-g260  ch85/g182r1519
    
    #定义需要爬取的页面数量，以及爬取链接
    def start_requests(self) :
        reqs = []
        # for i in range(10,96):  #ch10-96，
        #     for j in range(1,51):  #抓取的页面页码数量,最大可以设置51（总共50页）
        #         url = 'http://www.dianping.com/guangzhou/ch' + str(i) +'/p' + str(j)
        #         req = scrapy.Request(url)
        #         reqs.append(req)
        #美食ch10
        #gid = [210,103,111,113,116,117,132,114,110,102,207,217,219,115,109,34055,508,34014,104,118,251,250,1959,34032,101,106,107,3243,1338,246,26481,2714,247,1783]
        rid = [24,26,25,22,1549,621,1963,1964,27,1555,1552,1554]
        #美食ch30
        #gname = ['足疗按摩','酒吧','运动健身','文化艺术','茶馆','网吧网咖','棋牌室','KTV','游乐游艺','台球馆','洗浴/汗蒸','采摘/农家乐','DIY手工坊','桌面游戏','轰趴馆','真人CS','密室','私人影院','VR','更多休闲娱乐'] 
        gid=[141,133,2636,142,134,20042,32732,135,137,156,140,20038,144,6694,20040,20039,2754,20041,33857,26490]
        for i in gid:
            for j in rid:
                for m in range(1,51):
                    url = 'http://www.dianping.com/guangzhou/ch30/' + 'g' +str(i) +'r' + str(j) + 'p' + str(m)
                    req = scrapy.Request(url)
                    reqs.append(req)
        return reqs
        
    def parse(self, response) :
        item = Dp2Item()
        item['shop_name'] = response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[1]/a/h4/text()').extract()
        item['shop_class'] =  response.xpath('//*[@id="classfy"]/a[@class="cur"]/span/text()').extract()
        item['shop_city'] =  response.xpath('//*[@id="logo-input"]/div[1]/a[2]/span[2]/text()').extract()
        item['shop_zone'] =  response.xpath('//*[@id="region-nav"]/a[@class="cur"]/span/text()').extract()
        
        item['shop_address_1'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[3]/a[2]/span/text()').extract()
        item['shop_address_2'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[3]/span/text()').extract()
        #shop_tel
        item['shop_star'] = (response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[2]/span/@title').extract()
        item['com_num'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[2]/a[1]/b/text()').extract()
        item['price_avg'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[2]/a[2]/b/text()').extract()
        item['tag_name'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[3]/a[1]/span/text()').extract()
        item['kou_wei'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/span/span[1]/b/text()').extract()
        item['huan_jing'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/span/span[2]/b/text()').extract()
        item['fu_wu'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/span/span[3]/b/text()').extract()
        return item
