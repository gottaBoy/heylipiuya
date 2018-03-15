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
    start_urls = ['http://www.dianping.com/guangzhou/ch10/p1']  #ch10-96  p1-p50 g101-g260  ch85/g182r1519
    
    #定义需要爬取的页面数量，以及爬取链接
    def start_requests(self) :
        reqs = []
        for i in range(10,96):  #ch10-96，
            for j in range(1,51):  #抓取的页面页码数量,最大可以设置51（总共50页）
                url = 'http://www.dianping.com/guangzhou/ch' + str(i) +'/p' + str(j)
                req = scrapy.Request(url)
                reqs.append(req)
        return reqs
        
    def parse(self, response) :
        item = Dp2Item()
        item['shop_name'] = response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[1]/a/h4/text()').extract()
        item['shop_city'] =  response.xpath('//*[@id="logo-input"]/div[1]/a[2]/span[2]/text()').extract()
        item['shop_address_1'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[3]/a[2]/span/text()').extract()
        item['shop_address_2'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[3]/span/text()').extract()
        #shop_tel
        # item['shop_star'] = (response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[2]/span/'))[0].attrib.get('title')
        item['com_num'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[2]/a[1]/b/text()').extract()
        item['price_avg'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[2]/a[2]/b/text()').extract()
        item['tag_name'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[3]/a[1]/span/text()').extract()
        item['kou_wei'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/span/span[1]/b/text()').extract()
        item['huan_jing'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/span/span[2]/b/text()').extract()
        item['fu_wu'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/span/span[3]/b/text()').extract()
        return item
