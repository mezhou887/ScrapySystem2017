# -*- coding: utf-8 -*-

BOT_NAME = 'lianjia'

SPIDER_MODULES = ['lianjia.spiders']
NEWSPIDER_MODULE = 'lianjia.spiders'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 3

#SCHEDULER = "scrapy_redis.scheduler.Scheduler"    #调度
#DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  #去重
#SCHEDULER_PERSIST = True       #不清理Redis队列
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"    #队列


ITEM_PIPELINES = {
   'lianjia.pipelines.LianjiaPipeline': 300,
}

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = "lianjia"
MONGODB_DOCNAME = "saveinfo_5"

LOG_LEVEL = 'INFO'
