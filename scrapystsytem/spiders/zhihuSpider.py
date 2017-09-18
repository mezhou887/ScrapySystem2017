# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from scrapystsytem.items import ZhihuPeopleItem
from scrapy.selector import Selector
import logging
 
logger = logging.getLogger(__name__)
 
class ZhihuSpider(CrawlSpider):
    name = 'zhihu'
    allow_domains = ['zhihu.com']
    start_urls = [
        'https://www.zhihu.com/people/luo-wei-zi'
    ]
     
    rules = [
        Rule(sle(allow=('/people/[^/]+/followees$')), callback='parse_followees', follow=False),
        Rule(sle(allow=('/people/[^/]+/followers$')), callback='parse_followers', follow=False),
        Rule(sle(allow=("/people/[^/]+$", )), callback='parse_people_with_rules', follow=False),
    ]
     
    all_css_rules = {
        '.zm-profile-header': {
            '.zm-profile-header-clear': {
                '__use':'dump',
                'name':'.title-section .name::text',
                'sign':'.title-section .bio::text',
                'location':'.location.item::text',
                'business':'.business.item::text',
                'employment':'.employment.item::text',
                'position':'.position.item::text',
                'education':'.education.item::text',
                'education_extra':'.education-extra.item::text',
            }, '.zm-profile-header-operation': {
                '__use':'dump',
                'agree':'.zm-profile-header-user-agree strong::text',
                'thanks':'.zm-profile-header-user-thanks strong::text',
            }, '.profile-navbar': {
                '__use':'dump',
                'asks':'a[href*=asks] .num::text',
                'answers':'a[href*=answers] .num::text',
                'posts':'a[href*=posts] .num::text',
                'collections':'a[href*=collections] .num::text',
                'logs':'a[href*=logs] .num::text',
            },
        }, '.zm-profile-side-following': {
            '__use':'dump',
            'followees':'a.item[href*=followees] strong::text',
            'followers':'a.item[href*=followers] strong::text',
        }
    }
     
    def parse(self, response):
        print response.body
        return self._parse_response(response, self.parse_start_url, cb_kwargs={}, follow=True)    
     
    def parse_followees(self, response):
        return self.parse_people_with_rules(response);
     
    def parse_followers(self, response):
        return self.parse_people_with_rules(response);
     
    def parse_people_with_rules(self, response):
        item = self.parse_with_rules(response, self.all_css_rules, ZhihuPeopleItem);
        self.logger.info('Parsed'+response.url+'to '+str(item));
        return item;
     
    def parse_with_rules(self, response, rules, item_class):
        return self.dfs(Selector(response), rules, item_class);
         
    def dfs(self, sel, rules, item_class):
        if sel is None:
            return []
        item = item_class()
        self.traversal(sel, rules, item);
        return item;
     
    def traversal(self, sel, rules, item):
        if '__use' in rules:
            for nk, nv in rules.items():
                if nk == '__use':
                    continue
                if nk not in item:
                    item[nk] = []
                if sel.css(nv):
                    item[nk] += [i.extract() for i in sel.css(nv)]
                else:
                    item[nk] = []
        else:
            for nk, nv in rules.items():
                for i in sel.css(nk):
                    self.traversal(i, nv, item)
