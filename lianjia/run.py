# -*- coding: utf-8 -*-
'''
Created on 2017/07/11

@author: Administrator
'''

from scrapy import cmdline

# 启动文件
if __name__ =="__main__":
    cmdline.execute("scrapy crawl lianjiaspider".split());