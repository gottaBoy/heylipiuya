# -*- coding: utf-8 -*-
import json
import codecs
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Dp2Pipeline(object):
    
    def __init__(self):
        self.file = codecs.open("C:\my\E\my-python\dp2\data\shop_list.json",'wb',encoding = 'utf-8')

	def process_item(self, item, spider):
        
		for i in range(len(item['shop_name'])):
			print i
			shop_name = item['shop_name'][i]
			shop_city = item['shop_city'][0]
			shop_address_1 = item['shop_address_1'][i]
			shop_address_2 = item['shop_address_2'][i]
			#shop_tel
			com_num = item['com_num'][i]
			price_avg = item['price_avg'][i]
			tag_name = item['tag_name'][i]
			kou_wei = item['kou_wei'][i]
			huan_jing = item['huan_jing'][i]
			fu_wu = item['fu_wu'][i]
			dic = {
                "shop_name" : shop_name,
                "shop_city" : shop_city,
                "shop_address_1" : shop_address_1,
                "shop_address_2" : shop_address_2,
                #shop_tel,
                "com_num" : com_num,
                "price_avg" : price_avg,
                "tag_name" : tag_name,
                "kou_wei" : kou_wei,
                "huan_jing" : huan_jing,
                "fu_wu" : fu_wu,
            }
			dicts = json.dumps(dict(dic),ensure_ascii=False)
			line = dicts + ',' + '\n'
			self.file.write(line)
        
		print "*********************************"
		return item
        
	def close_spider(self,spider):
		self.file.close()
