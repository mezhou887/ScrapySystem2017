# -*- coding: utf-8 -*-
'''
Created on 2017年9月18日

@author: Administrator
'''
import logging
import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor as sle
from scrapy.selector import Selector
from scrapystsytem.items import CnbetaItem

logger = logging.getLogger(__name__)

class CnbetaSpider(CrawlSpider):
    name = 'cnbeta'
    allowed_domains = ['cnbeta.com']
    start_urls = [
        'http://www.cnbeta.com/'
    ]
     
    rules = [
        Rule(sle(allow=("/articles/.*\.htm")), callback='parse_cnbeta', follow=True),
    ]
    
    def parse_cnbeta(self, response):
        logger.debug('parse_cnbeta: '+response.url);
        articlelist = Selector(response).xpath('//div[@class="cnbeta-article"]');
        items = [];
        for article in articlelist: 
            item = CnbetaItem();
            item['title'] = article.xpath('header[@class="title"]/h1/text()').extract_first();
            item['publishtime']  = article.xpath('header[@class="title"]/div[@class="meta"]/span/text()').extract_first();
            
            logger.info('function: parse_cnbeta, url: '+response.url+' , item: '+str(item));
            items.append(item);
        return items;    