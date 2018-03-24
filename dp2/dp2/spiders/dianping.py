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
        # rid = [24,26,25,22,1549,621,1963,1964,27,1555,1552,1554]
        # rid = [24,26,25]
        rid = [1531,1960,30560,1532,1534,1959,1961,30561,1533,23050,1535,23049,1536,1965,1542,1541,1962,23051,7046,23053,1544,1543,1537,2602,1539,2096,2081,2095,7045,1538,1540]
        #yuch30
        #gname = ['足疗按摩','酒吧','运动健身','文化艺术','茶馆','网吧网咖','棋牌室','KTV','游乐游艺','台球馆','洗浴/汗蒸','采摘/农家乐','DIY手工坊','桌面游戏','轰趴馆','真人CS','密室','私人影院','VR','更多休闲娱乐'] 
        #gid=[141,133,2636,142,134,20042,32732,135,137,156,140,20038,144,6694,20040,20039,2754,20041,33857,26490]
        #电影演出赛事ch25
        #gname = ['电影院','演出','场馆','热门演出','艺术中心/文化广场','剧场/剧院','音乐厅/礼堂','其他电影演出赛']
        #gid=[136,25461,33880,33879,33877,33878,33882]
        #酒店
        #http://www.dianping.com/search/category/4/60

        #丽人ch50
        #http://www.dianping.com/search/category/4/50
        #gname = ['美发','美容/SPA','美甲美睫','医学美容','瑜伽','舞蹈','纹绣','瘦身纤体','纹身','祛痘','化妆品','产后塑形']
        # gid=[157,158,33761,183,148,149,2898,159,493,2572,123,2790]
        
        #运动健身ch45 p15
        # gname =['健身中心','游泳馆','漂流','羽毛球馆','台球馆','体育场馆','武术场馆','射箭馆','篮球场','保龄球馆','高尔夫场','足球场','网球场','乒乓球馆','壁球馆','溜冰场','更多运动场馆']
        # gid= [147,151,2838,152,156,150,6701,6709,146,155,154,6702,153,6712,6706,6713,145]

        #婚纱ch55 p15
        # gname = ['旅拍','海外婚礼','婚纱摄影','婚宴','婚戒首饰','婚纱礼服','婚庆公司','彩妆造型','婚礼跟拍','个性写真','婚车租赁','司仪主持','西服定制','婚礼小商品','更多婚礼服务']
        # gid= [33888,34057,163,165,191,162,167,166,185,6700,186,164,25412,192,6844]

        #购物ch20 p51
        # gname = ['服饰鞋包','综合商场','珠宝饰品','运动户外','免税店','超市/便利店','药店','化妆品','眼镜店','亲子购物','花店','数码产品','书店','家居建材','特色集市','食品','茶酒','水果生鲜','办公/文化用品','更多购物场所']
        # gid= [120,119,122,121,32739,187,235,123,128,125,26085,124,127,126,129,184,2714,26101,131]
        
        #学习培训ch75 p51
        # gname = ['外语培训','音乐培训','职业技术','升学辅导','美术培训','兴趣生活','驾校','教育院校','留学','更多教育培训']
        #gid= [2872,2873,2877,2876,2874,2878,179,260,32722,2882]
        
        # 广州周边游ch35 p20
        # gname=['景点','水上娱乐','展馆展览','动植物园','温泉','采摘/农家乐','旅游其他']
        # gid35=[33831,2916,2926,2834,5672,20038,33832]
        # for i in gid35:
        #     for j in rid:
        #         for m in range(1,21):
        #             url = 'http://www.dianping.com/guangzhou/ch35/' + 'g' +str(i) +'r' + str(j) + 'p' + str(m)
        #             req = scrapy.Request(url)
        #             reqs.append(req)
        
        # 广州生活服务ch80 p20
        # gname=['便民服务','金融','洗涤护理','家政','生活配送','房屋地产','旅行社','公司企业','商务服务','快照摄影','家电数码维修','文印图文','居家维修','售票点','老年生活','文化传媒','演出票务','交通','商圈','政府机构','网站','搬家运输','更多生活服务']
        # gid80 = [33971,34003,33762,195,2928,836,197,979,33958,3064,33976,3066,26117,980,34031,33965,25462,6823,2884,3082,26119,33986,26491]
        # for i in gid80:
        #     for j in rid:
        #         for m in range(1,21):
        #             url = 'http://www.dianping.com/guangzhou/ch80/' + 'g' +str(i) +'r' + str(j) + 'p' + str(m)
        #             req = scrapy.Request(url)
        #             reqs.append(req)
        
        # 广州医疗健康ch85 p30
        # gname=['医学美容','医院','齿科','中医','体检中心','药店','宠物医院','眼科医院','妇幼医院','精神卫生机构','皮肤病医院','妇科医院','其他医疗']
        # gid85 = [183,181,182,2914,612,235,25148,34053,257,34052,34051,34050,2912]
        # gid85 = [25148,34053,257,34052,34051,34050,2912]
        # for i in gid85:
        #     for j in rid:
        #         for m in range(1,31):
        #             url = 'http://www.dianping.com/guangzhou/ch85/' + 'g' +str(i) +'r' + str(j) + 'p' + str(m)
        #             req = scrapy.Request(url)
        #             reqs.append(req)

        # 广州爱车ch65 p30
        # gname=['停车场','维修保养','4S店/汽车销售','配件/车饰','汽车租赁','加油站','汽车美容']
        # gid65 = [180,176,175,177,178,236,20026]
        # for i in gid65:
        #     for j in rid:
        #         for m in range(1,31):
        #             url = 'http://www.dianping.com/guangzhou/ch65/' + 'g' +str(i) +'r' + str(j) + 'p' + str(m)
        #             req = scrapy.Request(url)
        #             reqs.append(req)
        
        # 广州宠物ch95 p11
        # gname=['宠物店','宠物食品用品','宠物医院','购宠','其他宠物']
        # gid95 = [25147,34042,25148,34043,34039]
        # for i in gid95:
        #     for j in rid:
        #         for m in range(1,12):
        #             url = 'http://www.dianping.com/guangzhou/ch95/' + 'g' +str(i) +'r' + str(j) + 'p' + str(m)
        #             req = scrapy.Request(url)
        #             reqs.append(req)
        
        # 广州电影ch30 p2
        # gid30 = [136]
        # for i in gid30:
        #     for j in rid:
        #         for m in range(1,3):
        #             url = 'http://www.dianping.com/guangzhou/ch30/' + 'g' +str(i) +'r' + str(j) + 'p' + str(m)
        #             req = scrapy.Request(url)
        #             reqs.append(req)

        #酒店hotel
        #fname = ['商务出行','休闲度假','青年旅社','情侣约会','会议酒店','亲子酒店','购物便捷','学校周边','交通枢纽','免费接机','主题乐园','复式酒店']
        fid = [74633,74626,74744,74905,74634,74627,74632,74630,74635,74629,74628,74641]
        # gname = ['经济型','三星/舒适','四星/高档','五星/豪华']
        gid = [171,3024,3022,3020]
        for i in fid:
            for g in gid:
                for j in rid:
                    for m in range(1,3):
                        url = 'http://www.dianping.com/guangzhou/hotel/' + 'f' +str(i) + 'g' + str(g) +'r' + str(j) + 'p' + str(m)
                        req = scrapy.Request(url)
                        reqs.append(req)
        return reqs

    def parse(self, response) :
        item = Dp2Item()
        item['hotel_name'] = response.xpath('//*[@class="hotelshop-list"]/li/div[1]/div[1]/h2/a[1]/text()').extract()
        item['hotel_class'] =  response.xpath('//*[@id="poi-list"]/div[2]/div[4]/div[1]/div[1]/a[@class="cur"]/span/text()').extract()
        item['hotel_city'] =  response.xpath('//*[@id="logo-input"]/div[1]/a[2]/span[2]/text()').extract()
        item['hotel_zone'] =  response.xpath('//*[@class="sub-filter-region-wrapper"]/a[@class="cur"]/span/text()').extract()
        
        item['hotel_address_1'] =  response.xpath('//*[@class="sub-filter-region-detail"]/a[@class="cur"]/span/text()').extract()
        item['hotel_address_2'] =  response.xpath('//*[@class="hotelshop-list"]/li/div[1]/div[1]/p[1]/span[1]/text()').extract()
        
        item['hotel_tags1'] =  response.xpath('//*[@class="hotelshop-list"]/li/div[1]/div[1]/p[2]/span[1]/text()').extract()
        item['hotel_tags2'] =  response.xpath('//*[@class="hotelshop-list"]/li/div[1]/div[1]/p[2]/span[2]/text()').extract()
        item['hotel_tags3'] =  response.xpath('//*[@class="hotelshop-list"]/li/div[1]/div[1]/p[2]/span[3]/text()').extract()
        item['hotel_tags4'] =  response.xpath('//*[@class="hotelshop-list"]/li/div[1]/div[1]/p[2]/span[4]/text()').extract()
        item['hotel_tags5'] =  response.xpath('//*[@class="hotelshop-list"]/li/div[1]/div[1]/p[2]/span[5]/text()').extract()

        item['hotel_star'] = response.xpath('//*[@id="poi-list"]/div[2]/div[2]/div[1]/div[1]/a[@class="cur"]/span/text()').extract()
        item['com_num'] =  response.xpath('//*[@class="hotelshop-list"]/li/div[1]/div[2]/div[1]/p[1]/strong[1]/text()').extract()
        item['price_avg'] =  response.xpath('//*[@class="hotelshop-list"]/li/div[1]/div[2]/div[2]/div[1]/div[1]/a[1]/text()').extract()
       
        return item
        
    # def parse(self, response) :
    #     item = Dp2Item()
    #     item['shop_name'] = response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[1]/a/h4/text()').extract()
    #     item['shop_class'] =  response.xpath('//*[@id="classfy"]/a[@class="cur"]/span/text()').extract()
    #     item['shop_city'] =  response.xpath('//*[@id="logo-input"]/div[1]/a[2]/span[2]/text()').extract()
    #     item['shop_zone'] =  response.xpath('//*[@id="region-nav"]/a[@class="cur"]/span/text()').extract()
        
    #     item['shop_address_1'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[3]/a[2]/span/text()').extract()
    #     item['shop_address_2'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[3]/span/text()').extract()
    #     #shop_tel
    #     item['shop_star'] = response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[2]/span/@title').extract()
    #     item['com_num'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[2]/a[1]/b/text()').extract()
    #     item['price_avg'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[2]/a[2]/b/text()').extract()
    #     item['tag_name'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[3]/a[1]/span/text()').extract()
    #     item['kou_wei'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/span/span[1]/b/text()').extract()
    #     item['huan_jing'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/span/span[2]/b/text()').extract()
    #     item['fu_wu'] =  response.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/span/span[3]/b/text()').extract()
    #     return item
