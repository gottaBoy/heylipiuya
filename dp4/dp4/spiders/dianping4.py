# -*- coding: utf-8 -*-
import scrapy
import time
import urllib2  
import random
import  xdrlib ,sys
import xlrd
from dp4.items import Dp4Item

class Dianping4Spider(scrapy.Spider):
    name = 'dianping4'
    allowed_domains = ['dianping.com']
    start_urls = ['http://www.dianping.com/guangzhou/ch0']
     
    # def __init__(self):
    #     self.tables = excel_table_byindex('dp4.xlsx',0,0)

    #定义需要爬取的页面数量，以及爬取链接
    def start_requests(self) :
        reqs = []
        # tables = excel_table_byindex(self,'dp4.xlsx',0,0) #打开excel
        list =[]
        file = 'C:/my/E/my-python/heylipiuya/dp4/dp4/dp4.xlsx'
        try:
            data = xlrd.open_workbook(file)
            print data 
            table = data.sheets()[0]
            nrows = table.nrows #行数
            # ncols = table.ncols #列数
            colnames =  table.row_values(0) #某一行数据 
            
            for rownum in range(1,nrows):

                row = table.row_values(rownum)
                if row:
                    app = {}
                    for i in range(len(colnames)):
                        app[colnames[i]] = row[i] 
                    list.append(app)
            for row in list:
                url = row["shop_url"]
            req = scrapy.Request("http://www.dianping.com/shop/98436557")
            reqs.append(req)
            return reqs
        except Exception,e:
            print str(e)
            return reqs
           
    def parse(self, response):
        item = Dp4Item()
        # 链接部分
        #  item['shop_url'] = response.xpath('//*[@id="shop-all-list"]/ul/li/div[1]/a/@href').extract()

        item['shop_name'] = response.xpath('//*[@class="breadcrumb"]/span/text()').extract()
        item['shop_city'] =  response.xpath('//*[@id="logo-input"]/div[1]/a[2]/span[2]/text()').extract()
        item['shop_address_1'] =  response.xpath('//div[@class="breadcrumb"]/a[3]/text()').extract()
        # item['shop_address_2'] =  response.xpath('//div[@class="breadcrumb"]/a[4]/text()').extract()
        item['shop_address_2'] =  response.xpath('//*[@id="basic-info"]/div[2]/span[2]/text()').extract()
        item['shop_tel'] =  response.xpath('//*[@id="basic-info"]/p/span[2]/text()').extract()
        
        item['shop_star'] = response.xpath('//*[@id="basic-info"]/div[1]/span[1]/text()').extract()
        item['com_num'] =  response.xpath('//*[@id="reviewCount"]/text()').extract()
        item['price_avg'] =  response.xpath('//*[@id="avgPriceTitle"]/text()').extract()
        
        item['tag_name1'] =  response.xpath('//*[@class="breadcrumb"]/a[1]/text()').extract()
        item['tag_name2'] = response.xpath('//*[@class="breadcrumb"]/a[2]/text()').extract()

        item['kou_wei'] =  response.xpath('//*[@id="comment_score"]/span[1]/text()').extract()
        item['huan_jing'] =  response.xpath('//*[@id="comment_score"]/span[2]/text()').extract()
        item['fu_wu'] =  response.xpath('//*[@id="comment_score"]/span[3]/text()').extract()

        item['shop_location'] = response.xpath('//*[@id="map"]/img/@src').extract()
        return item

    # def open_excel(self,file= 'dp4.xlsx'):
    #     try:
    #         data = xlrd.open_workbook(file)
    #         return data
    #     except Exception,e:
    #         print str(e)

    # def excel_table_byindex(self,file= 'dp4.xlsx',colnameindex=0,by_index=0):
    #     data = self.open_excel()
    #     table = data.sheets()[by_index]
    #     nrows = table.nrows #行数
    #     # ncols = table.ncols #列数
    #     colnames =  table.row_values(colnameindex) #某一行数据 
    #     list =[]
    #     for rownum in range(1,nrows):

    #         row = table.row_values(rownum)
    #         if row:
    #             app = {}
    #             for i in range(len(colnames)):
    #                 app[colnames[i]] = row[i] 
    #             list.append(app)
    #     return list
