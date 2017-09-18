# # -*- coding: utf-8 -*-
# '''
# Created on 2017年9月18日
#  
# @author: Administrator
# '''
# import logging
# import scrapy
# from scrapystsytem.misc.commonspider import CommonSpider
# from scrapy.spiders import Rule
# from scrapy.linkextractors import LinkExtractor as sle
# from scrapystsytem.items import DmoztoolsItem
#  
# logger = logging.getLogger(__name__)
#  
# class DmoztoolsSpider(CommonSpider):
#     name = "dmoztools"
#     allowed_domains = ["dmoztools.net"]
#     start_urls = [
#         "http://dmoztools.net/"
#     ]
#  
#     valid_categories = [
#         'Arts', 'Business', 'Computers', 'Games', 'Health', 'Home',
#         'Kids_and_Teens', 'News', 'Recreation', 'Reference', 'Regional', 'Science',
#         'Shopping', 'Society', 'Sports',
#     ]
#     
#     allow_rules = ['/'+i+'/' for i in valid_categories]
#     rules = [
#         Rule(sle(allow=allow_rules), callback='parse_1', follow=True),
#     ]
# 
#     item_rules = {
#         '.directory-url li': {
#             '__use': 'dump',
#             '__list': True,
#             'url': 'li > a::attr(href)',
#             'name': 'a::text',
#             'description': 'li::text',
#         }
#     }
# 
#     def parse_1(self, response):
#         logger.info('Parse depth 1 '+response.url)
#         items = self.parse_with_rules(response, self.item_rules, DmoztoolsItem)
#         return items
#     