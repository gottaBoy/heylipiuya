# -*- coding: utf-8 -*-

import openpyxl
import xlrd
# from openpyx import WorkBook  
# https://www.zhihu.com/collection/140778750
class Dp4ExcelPipeline(object):
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

    def open_spider(self, spider):
        '''
        create a queue
        :return:
        '''
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.append(['shop_name','shop_city','shop_address_1','shop_address_2','shop_tel','shop_star','com_num','price_avg','tag_name1','tag_name2','kou_wei','huan_jing','fu_wu','shop_location'])

    def process_item(self, item, spider):
        '''
        save every
        :return:
        '''
        self.log('process %s, %s:' % (spider.name, self.count + 1))
        if len(item['shop_name']) :
            shop_name = item['shop_name'][0]
            shop_city = item['shop_city'][0]  #str.split('|')[-1]
            shop_address_1 = item['shop_address_1'][0]
            shop_address_2 = item['shop_address_2'][0]
            shop_tel = item['shop_tel'][0]
            if len(item['shop_star']) :
                shop_star = item['shop_star'][0]
            else:
                shop_star = ''
            com_num = item['com_num'][0]
            price_avg = item['price_avg'][0]
            tag_name1 = item['tag_name1'][0]
            tag_name2 = item['tag_name2'][0]
            kou_wei = item['kou_wei'][0]
            huan_jing = item['huan_jing'][0]
            fu_wu = item['fu_wu'][0]
            if len(item['shop_location']) :
               shop_location = item['shop_location'][0].split('|')[-1]
            else:
                shop_location = ''
            line = [shop_name,shop_city,shop_address_1,shop_address_2,shop_tel,shop_star,com_num,price_avg,tag_name1,tag_name2,kou_wei,huan_jing,fu_wu,shop_location]
            self.ws.append(line)
       
        return item

    def close_spider(self, spider):
        '''
        save lines to excel
        :return:
        '''
        print 'ExcelPipline info:  items size: %s' % self.count
        # file_name = _generate_filename(spider, file_format='xlsx')
        file_name = 'dp4_ch10_data.xlsx'
        self.wb.save(file_name)

    def _generate_filename(self,spider, file_format): 
        pass
        # self.wb.open(file,) 
        # workbook = xlrd.open_workbook('dp2.xlsx')  
        # self.ws = workbook.sheet_by_name('Sheet1')  