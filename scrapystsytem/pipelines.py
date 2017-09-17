# -*- coding: utf-8 -*-
import json
import codecs
from collections import OrderedDict


class DoNothingPipeline(object):
    def process_item(self, item, spider):
        print spider.name
        return item


class JsonPipeline(object):

    def __init__(self):
        self.file = codecs.open('lianjia.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        print spider.name;
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        print spider.name;
        self.file.close();