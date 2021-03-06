# -*- coding: utf-8 -*-

# C:\Python27\Lib\site-packages\scrapy\settings

import sys
import os
from os.path import dirname
path = dirname(dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(path)

# Scrapy settings for scrapystsytem project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapystsytem'

SPIDER_MODULES = ['scrapystsytem.spiders']
NEWSPIDER_MODULE = 'scrapystsytem.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.25
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapystsytem.middlewares.ScrapystsytemSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapystsytem.misc.middleware.CustomUserAgentMiddleware': 543,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'scrapystsytem.pipeline.JsonPipeline.JsonPipeline': 300,
    'scrapystsytem.pipeline.MongoPipeline.PanduoduoMongoPipeline': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# # Email配置信息
# EXTENSIONS = {
#     'scrapy.extensions.statsmailer.StatsMailer': 500,
# }
# # 收件人
# STATSMAILER_RCPTS = ['mezhou887@foxmail.com']
# # 发件人
# MAIL_FROM = '1033738034@qq.com'
# MAIL_HOST = 'smtp.qq.com'
# MAIL_PORT = 465
# MAIL_TLS = True
# MAIL_SSL = True
# # 邮箱用户
# MAIL_USER = '1033738034@qq.com'
# # 邮箱密码
# MAIL_PASS = 'ghyftlmoejsgbeai'


# Log配置信息 
LOG_FILE = 'scrapysystem.log'
LOG_ENABLED = True
LOG_LEVEL = 'INFO' # CRITICAL > ERROR > WARNING > INFO > DEBUG


# Mongo配置信息
MONGODB_SERVER = "192.168.31.131"   
MONGODB_PORT = '27017'   
MONGODB_DB = 'zhihu' 
MONGO_USER='root'
MONGO_PASSWD='bitnami'

HTTPERROR_ALLOWED_CODES = [403,503]