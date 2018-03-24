# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Dp2Item(scrapy.Item):
    # define the fields for your item here like:
    # #店铺名称
    # shop_name = scrapy.Field()
    # #大类
    # shop_class = scrapy.Field()
    # #店铺所在城市
    # shop_city = scrapy.Field()
    # #大区
    # shop_zone = scrapy.Field()
    # #店铺所在区
    # shop_address_1 = scrapy.Field()
    # #店铺详细地址
    # shop_address_2 = scrapy.Field()

    # #shop_tel = scrapy.Field()
    # shop_star = scrapy.Field()
    # #评论数
    # com_num = scrapy.Field()
    # #人均消费
    # price_avg = scrapy.Field()
    # #所属类别
    # tag_name = scrapy.Field()
    # #口味评分
    # kou_wei = scrapy.Field()
    # #环境评分
    # huan_jing = scrapy.Field()
    # #服务评分
    # fu_wu = scrapy.Field()

    # 酒店
    #店铺名称
    hotel_name = scrapy.Field()
    #大类
    hotel_class = scrapy.Field()
    #店铺所在城市
    hotel_city = scrapy.Field()
    #大区
    hotel_zone = scrapy.Field()
    #店铺所在区
    hotel_address_1 = scrapy.Field()
    #店铺详细地址
    hotel_address_2 = scrapy.Field()

    #hotel_tel = scrapy.Field()
    hotel_star = scrapy.Field()
    #评论数
    com_num = scrapy.Field()
    #人均消费
    price_avg = scrapy.Field()
    hotel_tags1 = scrapy.Field()
    hotel_tags2 = scrapy.Field()
    hotel_tags3 = scrapy.Field()
    hotel_tags4 = scrapy.Field()
    hotel_tags5 = scrapy.Field()

