# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Dp4Item(scrapy.Item):
    # define the fields for your item here like:
     #店铺名称
    shop_name = scrapy.Field()
    #店铺所在城市
    shop_city = scrapy.Field()
    #店铺所在区
    shop_address_1 = scrapy.Field()
    #店铺详细地址
    shop_address_2 = scrapy.Field()
    #店铺经纬度
    shop_location = scrapy.Field()
    #店铺联系方式
    shop_tel = scrapy.Field()
    #星级
    shop_star = scrapy.Field()
    #评论数
    com_num = scrapy.Field()
    #人均消费
    price_avg = scrapy.Field()
    #所属类别
    tag_name1 = scrapy.Field()
    tag_name2 = scrapy.Field()
    #口味评分
    kou_wei = scrapy.Field()
    #环境评分
    huan_jing = scrapy.Field()
    #服务评分
    fu_wu = scrapy.Field()
