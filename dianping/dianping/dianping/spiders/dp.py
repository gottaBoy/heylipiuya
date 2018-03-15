# -*- coding: utf-8 -*-
import scrapy
import time
import urllib2  
import random  
from dianping.items import DianpingItem

class DpSpider(scrapy.Spider):
    name = 'dp'
    allowed_domains = ['dianping.com']
    start_urls = ['https://www.dianping.com/search/category/1/10/o3p1']
    #定义需要爬取的页面数量，以及爬取链接
    def start_requests(self):
		reqs = []
		for i in range(1,30):#抓取的城市数字代码,最大可以设置991，
			for j in range(1,30):#抓取的页面页码数量,最大可以设置51（总共50页）
				url = 'https://www.dianping.com/search/category/' + str(i) +'/10/o3p' + str(j)
				req = scrapy.Request(url)
				reqs.append(req)
		return reqs
    def parse(self, response):
		item = DianpingItem()
		item['shop_name'] = response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[1]/a/h4/text()').extract()
		item['shop_city'] =  response.xpath('//*[@id="page-header"]/div[1]/a[2]/text()').extract()
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

"""
        item =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[1]/a/h4').extract()
        for i in item:
        	print i
        print "****************"

        item =  response.xpath('//*[@id="page-header"]/div[1]/a[2]/text()').extract()
        for i in item:
        	print i
        print "****************"

        item =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[3]/a[2]/span').extract()
        for i in item:
        	print i
        print "****************"

        item =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[3]/span').extract()
        for i in item:
        	print i
        print "****************"

        #tag_name
        item =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[3]/a[1]/span/text()').extract()
        for i in item:
        	print i
        	time.sleep(1)
        print "****************"

        #com_num
        item =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[2]/a[1]/b/text()').extract()
        for i in item:
        	print i
        	time.sleep(1)
        print "****************"

        #price
        item =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[2]/a[2]/b/text()').extract()
        for i in item:
        	print i
        	time.sleep(1)
        print "****************"

        #kouwei
        item =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/span/span[1]/b/text()').extract()
        for i in item:
        	print i
        	time.sleep(1)
        print "****************"

        #huanjing
        item =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/span/span[2]/b/text()').extract()
        for i in item:
        	print i
        	time.sleep(1)
        print "****************"

        #fuwu
        item =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/span/span[3]/b/text()').extract()
        for i in item:
        	print i
        	time.sleep(1)
        print "****************"

        time.sleep(1)
        return item
"""
