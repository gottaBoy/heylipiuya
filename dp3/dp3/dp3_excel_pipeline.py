# -*- coding: utf-8 -*-

import openpyxl
import xlrd
# from openpyx import WorkBook  
# https://www.zhihu.com/collection/140778750
class Dp3ExcelPipeline(object):
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
        # self.ws.append(['shop_name','shop_city','shop_address_1','shop_address_2','com_num','price_avg','tag_name','kou_wei','huan_jing','fu_wu'])
        self.ws.append(['shop_url'])

    def process_item(self, item, spider):
        '''
        save every
        :return:
        '''
        self.log('process %s, %s:' % (spider.name, self.count + 1))
        
        # for i in range(len(item['shop_name'])):
    	# 	print i
        #         shop_name = item['shop_name'][i]
        #         shop_city = item['shop_city'][0]
                
        #         if(len(item['shop_address_1'])<=i):
        #                shop_address_1 = ''
        #         else:
        #            shop_address_1 = item['shop_address_1'][i]

        #         if(len(item['shop_address_2'])<=i):
        #                shop_address_2 = ''
        #         else:
        #            shop_address_2 = item['shop_address_2'][i]
        #         #shop_tel
        #         if(len(item['com_num'])<=i):
        #                com_num = ''
        #         else:
        #            com_num = item['com_num'][i]

        #         if(len(item['price_avg'])<=i):
        #            price_avg = ''
        #         else:
        #            price_avg = item['price_avg'][i]
                
        #         if(len(item['tag_name'])<=i):
        #             tag_name = ''
        #         else:
        #             tag_name = item['tag_name'][i]

        #         if(len(item['kou_wei'])<=i):
        #             kou_wei = ''
        #         else:
        #             kou_wei = item['kou_wei'][i]

        #         if(len(item['huan_jing'])<=i):
        #             huan_jing = ''
        #         else:
        #             huan_jing = item['huan_jing'][i]

        #         if(len(item['fu_wu'])<=i):
        #             fu_wu = ''
        #         else:
        #             fu_wu = item['fu_wu'][i]

        #         line = [shop_name,shop_city,shop_address_1,shop_address_2,com_num,price_avg,tag_name,kou_wei,huan_jing,fu_wu]
        #         self.ws.append(line)
        for i in range(len(item['shop_url'])):
        	print i
                shop_url = item['shop_url'][i]
                line = [shop_url]
                self.ws.append(line)
        return item

    def close_spider(self, spider):
        '''
        save lines to excel
        :return:
        '''
        print 'ExcelPipline info:  items size: %s' % self.count
        # file_name = _generate_filename(spider, file_format='xlsx')
        file_name = 'dp3_ch10_url.xlsx'
        self.wb.save(file_name)

    def _generate_filename(self,spider, file_format): 
        pass
        # self.wb.open(file,) 
        # workbook = xlrd.open_workbook('dp2.xlsx')  
        # self.ws = workbook.sheet_by_name('Sheet1')  