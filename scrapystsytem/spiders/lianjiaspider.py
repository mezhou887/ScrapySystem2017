# # -*- coding: utf-8 -*-
# import requests, re, scrapy, logging
# from scrapy.selector import Selector
# from scrapy.spiders import Spider
# from scrapystsytem.items import LianjiaItem
# 
# logger = logging.getLogger(__name__)
# 
# 
# import pprint
# class MyPrettyPrinter(pprint.PrettyPrinter):
#     def format(self, object, context, maxlevels, level):
#         if isinstance(object, unicode):
#             return (object.encode('utf8'), True, False)
#         return pprint.PrettyPrinter.format(self, object, context, maxlevels, level)
# pp = MyPrettyPrinter()
# 
# class LianjiaspiderSpider(Spider):
# 
#     name = 'lianjia'
#     allowed_domains = ['lianjia.com']
#     start_urls = [
#         'http://hz.lianjia.com/ershoufang/'
#     ]
# 
#     def parse(self, response):
#         sel = Selector(response);
#         area_list = sel.xpath('//div[@class="m-filter"]/div/dl/dd/div[1]/div/a')
#         for area in area_list:
#             area_han = area.xpath('text()').extract_first()                 # 地点
#             area_pin = area.xpath('@href').extract_first().split('/')[2]   # 拼音
#             area_url = 'http://hz.lianjia.com/ershoufang/{}/'.format(area_pin)
#             logger.info('area_url: '+area_url)
#             yield scrapy.Request(url=area_url, callback=self.parse_list, meta={"id1":area_han,"id2":area_pin})
# 
# 
#     def parse_list(self, response):
#         for i in range(1,5):
#             list_url = 'http://hz.lianjia.com/ershoufang/{}/pg{}/'.format(response.meta["id2"],str(i))
#             yield scrapy.Request(url=list_url, callback=self.parse_detail, meta={"id1":response.meta["id1"],"id2": response.meta["id2"]})
# 
# 
#     def parse_detail(self, response):
#             house_list = Selector(response).xpath('//ul[@class="sellListContent"]/li')
#             items = []
#             for house in house_list:
#                 item = LianjiaItem()
#                 item['title'] = house.xpath('div[1]/div[1]/a/text()').extract_first()
#                 item['community'] = house.xpath('div[1]/div[2]/div/a/text()').extract_first()
#                 item['model'] = house.xpath('div[1]/div[2]/div/text()').extract_first().split('|')[1]
#                 item['area'] = house.xpath('div[1]/div[2]/div/text()').extract_first().split('|')[2]
#                 item['focus_num'] = house.xpath('div[1]/div[4]/text()').extract_first().split('/')[0]
#                 item['watch_num'] = house.xpath('div[1]/div[4]/text()').extract_first().split('/')[1]
#                 item['time'] = house.xpath('div[1]/div[4]/text()').extract_first().split('/')[2]
#                 item['price'] = house.xpath('div[1]/div[6]/div[1]/span/text()').extract_first()
#                 item['average_price'] = house.xpath('div[1]/div[6]/div[2]/span/text()').extract_first()
#                 item['link'] = house.xpath('div[1]/div[1]/a/@href').extract_first()
#                 item['city'] = response.meta["id1"]
#                 self.url_detail = house.xpath('div[1]/div[1]/a/@href').extract_first()
#                 item['Latitude'] = self.get_latitude(self.url_detail)
#                 items.append(item)
#                 
#                 pp.pprint(item)
#                 logger.info('Parsed'+response.url+'to '+str(item))
#             return items;            
# 
#     def get_latitude(self,url):  # 进入每个房源链接抓经纬度
#         body = requests.get(url)
#         latitude = Selector(text=body.text).xpath('/html/body/script[20]/text()').extract_first()
#         regex = '''resblockPosition(.+)'''
#         items = re.search(regex, latitude)
#         content = items.group()[:-1]  # 经纬度
#         longitude_latitude = content.split(':')[1]
#         return longitude_latitude[1:-1]