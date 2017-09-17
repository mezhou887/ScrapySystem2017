# -*- coding: utf-8 -*-

import random
from scrapystsytem.misc.agent import AGENTS
from scrapystsytem.misc.proxy import PROXIES

class CustomUserAgentMiddleware(object):
    
    def process_request(self, request, spider):
        print spider.name
        agent = random.choice(AGENTS)
        request.headers['User-Agent'] = agent


class CustomHttpProxyMiddleware(object):

    def process_request(self, request, spider):
        print spider.name
        p = random.choice(PROXIES)
        request.meta['proxy'] = "http://%s" % p['ip_port']