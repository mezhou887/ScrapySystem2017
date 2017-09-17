# -*- coding: utf-8 -*-
'''
Created on 2017年9月10日

@author: Administrator
'''

from scrapy import cmdline
if __name__ =="__main__":
    cmdline.execute("scrapy crawl cnbeta -o cnbeta.csv -s CLOSESPIDER_ITEMCOUNT=5".split());
#     cmdline.execute("scrapy crawl lianjia -o lianjia.csv -s CLOSESPIDER_ITEMCOUNT=5".split());
#     cmdline.execute("scrapy crawl quites -o quites.csv".split());
#     cmdline.execute("scrapy crawl car".split());
    
    