# -*- coding: utf-8 -*-

from pymongo import MongoClient

class PanduoduoMongoPipeline(object):
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
        