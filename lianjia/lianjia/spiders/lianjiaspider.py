# -*- coding: utf-8 -*-
import scrapy
import requests
import re
import time
from ..items import LianjiaItem
from scrapy.selector import Selector
#from scrapy_redis.spiders import RedisSpider

# 主要运行文件
class LianjiaspiderSpider(scrapy.Spider):
    name = 'lianjiaspider'
    redis_key = 'lianjiaspider:urls'    # 名字是由RedisMixin类来确定的
    start_urls = 'http://bj.lianjia.com/ershoufang/'

    # 覆盖父类的同名方法是要加入自己的user_agent
    def start_requests(self):
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'
        headers = {'User-Agent': user_agent}
        yield scrapy.Request(url=self.start_urls, headers=headers, method='GET', callback=self.parse)

    # 得到每个区域的拼音名称
    def parse(self, response):
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'
        headers = {'User-Agent': user_agent}
        sel = Selector(response)
        area_list = sel.xpath('//div[@class="m-filter"]/div/dl/dd/div[1]/div/a')
        print area_list
        for area in area_list:
            try:
                area_han = area.xpath('text()').extract_first()    # 地点
                area_pin = area.xpath('@href').extract_first().split('/')[2]   # 拼音
                if area_pin == 'lf.lianjia.com': # 燕郊和香河不在这里
                    break
                area_url = 'http://bj.lianjia.com/ershoufang/{}/'.format(area_pin)
                yield scrapy.Request(url=area_url, headers=headers, callback=self.detail_url, meta={"id1":area_han,"id2":area_pin} )
            except Exception:
                pass

    def get_latitude(self,url):  # 进入每个房源链接抓经纬度
        body = requests.get(url)
        latitude = Selector(text=body.text).xpath('/html/body/script[20]/text()').extract_first()
        time.sleep(3)
        regex = '''resblockPosition(.+)'''
        items = re.search(regex, latitude)
        content = items.group()[:-1]  # 经纬度
        longitude_latitude = content.split(':')[1]
        print longitude_latitude[1:-1]
        return longitude_latitude[1:-1]

    def detail_url(self,response):
        'http://bj.lianjia.com/ershoufang/dongcheng/pg2/'
        for i in range(1,101):
            url = 'http://bj.lianjia.com/ershoufang/{}/pg{}/'.format(response.meta["id2"],str(1))
            time.sleep(3)
            try:
                body = requests.get(url)
                houselist = Selector(text=body.text).xpath('//ul[@class="sellListContent"]/li')
                for house in houselist:
                    try:
                        item = LianjiaItem()
                        item['title'] = house.xpath('div[1]/div[1]/a/text()').extract_first()
                        item['community'] = house.xpath('div[1]/div[2]/div/a/text()').extract_first()
                        item['model'] = house.xpath('div[1]/div[2]/div/text()').extract_first().split('|')[1]
                        item['area'] = house.xpath('div[1]/div[2]/div/text()').extract_first().split('|')[2]
                        item['focus_num'] = house.xpath('div[1]/div[4]/text()').extract_first().split('/')[0]
                        item['watch_num'] = house.xpath('div[1]/div[4]/text()').extract_first().split('/')[1]
                        item['time'] = house.xpath('div[1]/div[4]/text()').extract_first().split('/')[2]
                        item['price'] = house.xpath('div[1]/div[6]/div[1]/span/text()').extract_first()
                        item['average_price'] = house.xpath('div[1]/div[6]/div[2]/span/text()').extract_first()
                        item['link'] = house.xpath('div[1]/div[1]/a/@href').extract_first()
                        item['city'] = response.meta["id1"]
                        self.url_detail = house.xpath('div[1]/div[1]/a/@href').extract_first()
                        item['Latitude'] = self.get_latitude(self.url_detail)
                    except Exception:
                        pass
                    yield item
            except Exception:
                pass
