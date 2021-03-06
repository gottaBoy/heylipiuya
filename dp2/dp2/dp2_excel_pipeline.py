# -*- coding: utf-8 -*-

import openpyxl
import xlrd
# from openpyx import WorkBook  
# https://www.zhihu.com/collection/140778750
class Dp2ExcelPipeline(object):
    '''
    use Item Exporter
    save the item to excel
    '''

    def __init__(self):
        '''
        initialize the object
        '''
        self.spider = None
        self.count = 0

    def log(self, l):
        '''
        reload the log
        :return:
        '''
        msg = '========== CdcspiderExcelPipeline ==  %s' % l

        if self.spider is not None:
            # spider.logger -> return logging.LoggerAdapter(logger, {'spider': self})
            self.spider.logger.info(msg)

    # def open_spider(self, spider):
    #     '''
    #     create a queue
    #     :return:
    #     '''
    #     self.wb = openpyxl.Workbook()
    #     self.ws = self.wb.active
    #     self.ws.append(['shop_name','shop_class','shop_city','shop_zone','shop_address_1','shop_address_2','shop_star','com_num','price_avg','tag_name','kou_wei','huan_jing','fu_wu'])

    # def process_item(self, item, spider):
    #     '''
    #     save every
    #     :return:
    #     '''
    #     self.log('process %s, %s:' % (spider.name, self.count + 1))

    #     for i in range(len(item['shop_name'])):
    # 		print i
    #             shop_name = item['shop_name'][i]
    #             #shop_class = item['shop_class'][0]
    #             shop_class = ''
    #             shop_city = item['shop_city'][0]
    #             shop_zone = item['shop_zone'][0]
                
    #             if(len(item['shop_address_1'])<=i):
    #                    shop_address_1 = ''
    #             else:
    #                shop_address_1 = item['shop_address_1'][i]

    #             if(len(item['shop_address_2'])<=i):
    #                 shop_address_2 = ''
    #             else:
    #                shop_address_2 = item['shop_address_2'][i]
                
    #             if(len(item['shop_star'])<=i):
    #                 shop_star = ''
    #             else:
    #                 shop_star = item['shop_star'][i]
    #             #shop_tel
    #             if(len(item['com_num'])<=i):
    #                    com_num = ''
    #             else:
    #                com_num = item['com_num'][i]

    #             if(len(item['price_avg'])<=i):
    #                price_avg = ''
    #             else:
    #                price_avg = item['price_avg'][i]
                
    #             if(len(item['tag_name'])<=i):
    #                 tag_name = ''
    #             else:
    #                 tag_name = item['tag_name'][i]

    #             if(len(item['kou_wei'])<=i):
    #                 kou_wei = ''
    #             else:
    #                 kou_wei = item['kou_wei'][i]

    #             if(len(item['huan_jing'])<=i):
    #                 huan_jing = ''
    #             else:
    #                 huan_jing = item['huan_jing'][i]

    #             if(len(item['fu_wu'])<=i):
    #                 fu_wu = ''
    #             else:
    #                 fu_wu = item['fu_wu'][i]

    #             line = [shop_name,shop_class,shop_city,shop_zone,shop_address_1,shop_address_2,shop_star,com_num,price_avg,tag_name,kou_wei,huan_jing,fu_wu]
    #             self.ws.append(line)
    #     return item

    def open_spider(self, spider):
        '''
        create a queue
        :return:
        '''
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.append(['hotel_name','hotel_class','hotel_city','hotel_zone','hotel_address_1','hotel_address_2','hotel_star','com_num','price_avg','hotel_tags1','hotel_tags2','hotel_tags3','hotel_tags4','hotel_tags5'])
   
    def process_item(self, item, spider):
        '''
        save every
        :return:
        '''
        self.log('process %s, %s:' % (spider.name, self.count + 1))

        for i in range(len(item['hotel_name'])):
    		print i
                hotel_name = item['hotel_name'][i]
                
                if(len(item['hotel_class'])<=i):
                    hotel_class = ''
                else:
                   hotel_class = item['hotel_class'][i]

                hotel_city = item['hotel_city'][0]

                if(len(item['hotel_zone'])<=i):
                    hotel_zone = ''
                else:
                   hotel_zone = item['hotel_zone'][i]
                
                
                if(len(item['hotel_address_1'])<=i):
                       hotel_address_1 = ''
                else:
                   hotel_address_1 = item['hotel_address_1'][i]

                if(len(item['hotel_address_2'])<=i):
                    hotel_address_2 = ''
                else:
                   hotel_address_2 = item['hotel_address_2'][i]
                
                if(len(item['hotel_star'])<=i):
                    hotel_star = ''
                else:
                    hotel_star = item['hotel_star'][i]
                
                if(len(item['com_num'])<=i):
                       com_num = ''
                else:
                   com_num = item['com_num'][i]

                if(len(item['price_avg'])<=i):
                   price_avg = ''
                else:
                   price_avg = item['price_avg'][i]
                
                if(len(item['hotel_tags1'])<=i):
                    hotel_tags1 = ''
                else:
                    hotel_tags1 = item['hotel_tags1'][i]

                if(len(item['hotel_tags2'])<=i):
                    hotel_tags2 = ''
                else:
                    hotel_tags2 = item['hotel_tags2'][i]

                if(len(item['hotel_tags3'])<=i):
                    hotel_tags3 = ''
                else:
                    hotel_tags3 = item['hotel_tags3'][i]

                if(len(item['hotel_tags4'])<=i):
                    hotel_tags4 = ''
                else:
                    hotel_tags4 = item['hotel_tags4'][i]

                if(len(item['hotel_tags5'])<=i):
                    hotel_tags5 = ''
                else:
                    hotel_tags5 = item['hotel_tags5'][i]

                line = [hotel_name,hotel_class,hotel_city,hotel_zone,hotel_address_1,hotel_address_2,hotel_star,com_num,price_avg,hotel_tags1,hotel_tags2,hotel_tags3,hotel_tags4,hotel_tags5]
                self.ws.append(line)
        return item

    def close_spider(self, spider):
        '''
        save lines to excel
        :return:
        '''
        print 'ExcelPipline info:  items size: %s' % self.count
        # file_name = _generate_filename(spider, file_format='xlsx')
        file_name = 'dp2_ch_hotel_data.xlsx'
        self.wb.save(file_name)

    # def _generate_filename(spider, file_format): 
    #     pass
        # self.wb.open(file,) 
        # workbook = xlrd.open_workbook('dp2.xlsx')  
        # self.ws = workbook.sheet_by_name('Sheet1')  