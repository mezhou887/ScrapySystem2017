# -*- coding: utf-8 -*-
import json
import codecs
from collections import OrderedDict
from pymongo import MongoClient
from scrapy.exceptions import DropItem


class DoNothingPipeline(object):
    def process_item(self, item, spider):
        print spider.name
        return item
 
 
class JsonPipeline(object):
    max_dropcount = 10         # 抓取数量
    current_dropcount = 0      # 当前数量
 
    def __init__(self):
        self.file = codecs.open('panduoduo.json', 'w', encoding='utf-8')
 
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
        

class MongoPipeline(object):
    collection_panduoduo = 'panduoduo'

    def __init__(self, mongo_server, mongo_port, mongo_db, mongo_user, mongo_passwd):
        self.mongo_server = mongo_server
        self.mongo_port = mongo_port
        self.mongo_db = mongo_db
        self.mongo_user = mongo_user
        self.mongo_passwd = mongo_passwd

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_server=crawler.settings.get('MONGODB_SERVER'),
            mongo_port=crawler.settings.get('MONGODB_PORT'),
            mongo_db=crawler.settings.get('MONGODB_DB'),
            mongo_user=crawler.settings.get('MONGO_USER'),
            mongo_passwd=crawler.settings.get('MONGO_PASSWD')
        )

    def open_spider(self, spider):
        uri = "mongodb://%s:%s@%s:%s" % (self.mongo_user, self.mongo_passwd, self.mongo_server, self.mongo_port)
        self.client = MongoClient(uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_panduoduo].insert(dict(item))
        return item
        