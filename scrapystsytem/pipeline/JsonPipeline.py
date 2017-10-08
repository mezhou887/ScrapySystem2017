'''
Created on 2017年10月8日

@author: Administrator
'''

import json
import codecs
from collections import OrderedDict
from scrapy.exceptions import DropItem


class JsonPipeline(object):
    max_dropcount = 10         # 抓取数量
    current_dropcount = 0      # 当前数量
 
    def __init__(self):
        self.file = codecs.open(self.name + '.json', 'w', encoding='utf-8')
 
    def process_item(self, item, spider):
        self.current_dropcount += 1
        if(self.current_dropcount >= self.max_dropcount):
            spider.close_down = True
            raise DropItem("reach max limit")        

        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False) + "\n"
        self.file.write(line)
        return item
 
    def spider_closed(self, spider):
        print spider.name;
        self.file.close();
