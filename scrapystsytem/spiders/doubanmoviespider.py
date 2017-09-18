# -*- coding: utf-8 -*-
import logging
from scrapystsytem.misc.commonspider import CommonSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor as sle
  
logger = logging.getLogger(__name__)
  
class DoubanMovieSpider(CommonSpider):
    name = "doubanmovie"
    allowed_domains = ["douban.com"]
    start_urls = [
        "https://movie.douban.com/chart"
    ]

    rules = [
        Rule(sle(allow=("/subject/[0-9]+/$")), callback='parse_subject', follow=True),
    ]
  
    content_css_rules = {
        'rating_per': '.rating_per::text',
        'rating_num': '.rating_num::text',
        'title': 'h1 span:nth-child(1)::text',
        'rating_people': '.rating_people span::text',
    }
  
    def parse_subject(self, response):
        item = self.parse_with_rules(response, self.content_css_rules, dict)
        logger.info('function: parse_subject, url: '+response.url+' , item: '+str(item));
        return item