# -*- coding: utf-8 -*-
'''
Created on 2017年10月5日

@author: Administrator
'''
import scrapy
from scrapystsytem.items import PanduoduoItem
from scrapy.exceptions import CloseSpider

class Panduoduo(scrapy.Spider):
    name = 'panduoduo'
    allowed_domains =['panduoduo.net']
    start_urls = ['http://www.panduoduo.net/c/4/{}'.format(n) for n in range(1,86151)]#6151
    close_down = False
    
    
    def parse(self, response):
        base_url = 'http://www.panduoduo.net'
        node_list = response.xpath("//table[@class='list-resource']/tr")
        for node  in node_list:
            duoItem = PanduoduoItem()
            title = node.xpath("./td[@class='t1']/a/text()").extract()
            duoItem['docName'] = ''.join(title)
            link = node.xpath("./td[@class='t1']/a/@href").extract()
            linkUrl  = base_url+''.join(link)
            duoItem['docLink'] = linkUrl
            docType = node.xpath("./td[2]/a/text()").extract()
            duoItem['docType'] = ''.join(docType)
            docSize = node.xpath("./td[@class='t2']/text()").extract()
            duoItem['docSize'] = ''.join(docSize)
            docCount = node.xpath("./td[5]/text()").extract()
            docTime = node.xpath("./td[6]/text()").extract()
            duoItem['docCount'] = ''.join(docCount)
            duoItem['docTime'] = ''.join(docTime)
            yield duoItem
            
            if(self.close_down == True):
                raise CloseSpider(reason = "达到抓取数量") 
