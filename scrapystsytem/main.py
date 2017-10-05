# -*- coding: utf-8 -*-
'''
Created on 2017年9月10日

@author: Administrator
'''

import os

from scrapy import cmdline
if __name__ =="__main__":
    
    for fpathe,dirs,fs in os.walk(os.path.abspath('.')):
        for f in fs:
            if f.endswith('.pyc') or f.endswith('.csv')or f.endswith('.json'):
                os.remove(os.path.join(fpathe,f));    
    
#     cmdline.execute("scrapy crawl cnbeta -o cnbeta.csv -s CLOSESPIDER_ITEMCOUNT=5".split())
#     cmdline.execute("scrapy crawl quote -o quote.csv".split())
#     cmdline.execute("scrapy crawl doubanmovie -o doubanmovie.csv".split())
#     cmdline.execute("scrapy crawl dmoztools -o dmoztools.csv".split())
    cmdline.execute("scrapy crawl panduoduo".split())
#     cmdline.execute("scrapy crawl manong -o manong.csv -s CLOSESPIDER_ITEMCOUNT=5".split())
#     cmdline.execute("scrapy crawl lianjia -o lianjia.csv -s CLOSESPIDER_ITEMCOUNT=5".split())
#     cmdline.execute("scrapy crawl car".split());
    
    