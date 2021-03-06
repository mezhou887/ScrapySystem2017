# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.org/en/latest/topics/items.html

from scrapy import Field,Item

class PanduoduoItem(Item):
    docName     = Field()
    docLink     = Field()
    docType     = Field()
    docSize     = Field()
    docPTpye    = Field()
    docCount    = Field()
    docTime     = Field()


class DmoztoolsItem(Item):
    url         = Field()
    name        = Field()
    description = Field()

class CnbetaItem(Item):
    title         = Field()
    publishtime   = Field()

class LianjiaItem(Item):
    # 标签  小区  户型   面积   关注人数  观看人数  发布时间  价格   均价  详情链接  经纬度 城区
    title         = Field()
    community     = Field()
    model         = Field()
    area          = Field()
    focus_num     = Field()
    watch_num     = Field()
    time          = Field()
    price         = Field()
    average_price = Field()
    link          = Field()
    city          = Field()
   
   
class ZhihuPeopleItem(Item):
    id              = Field()
    name            = Field()
    sign            = Field()
    location        = Field()
    business        = Field()
    employment      = Field()
    position        = Field()
    education       = Field()
    education_extra = Field()
    description     = Field()
    agree           = Field()
    thanks          = Field()
    asks            = Field()
    answers         = Field()
    posts           = Field()
    collections     = Field()
    logs            = Field()
    followees       = Field()
    followers       = Field()
    follow_topics   = Field() 
    
class XiCiDaiLiItem(Item):
    ip              = Field()
    port            = Field()
    position        = Field()
    type            = Field()
    speed           = Field()
    last_check_time = Field()