# -*- coding: utf-8 -*-
import logging
import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor as sle
from scrapy.selector import Selector
logger = logging.getLogger(__name__)


class PcautoSpider(CrawlSpider):
    name = 'pcauto'
    allowed_domains = ['pcauto.com.cn']
    start_urls = [
        'http://www.pcauto.com.cn/'
    ]     
    
    rules = [
        Rule(sle(allow=("/car/(0-){11}\d*/")), callback='parse_list', follow=True),
        Rule(sle(allow=("com\.cn/m\d*/$")), callback='parse_info', follow=True),
    ]   
    
    def parse_info(self, response):
        logger.info(response.body)
        logger.info('info page: %s', response.url);
        sel = Selector(response)
        
        
    def parse_list(self, response):
        logger.info(response.body)
        logger.info('list page: %s', response.url);
        sel = Selector(response)
        
        
        