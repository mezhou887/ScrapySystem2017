# -*- coding: utf-8 -*-

import random
import json
from scrapystsytem.misc.agent import AGENTS
from scrapystsytem.misc.proxy import PROXIES

class CustomUserAgentMiddleware(object):
    
    def process_request(self, request, spider):
        agent = random.choice(AGENTS)
        request.headers['User-Agent'] = agent


class CustomHttpProxyMiddleware(object):

    def process_request(self, request, spider):
        p = random.choice(PROXIES)
        request.meta['proxy'] = "http://%s" % p['ip_port']
        
class CookiesMiddleware(object):
    
    """ 换Cookie """
    cookie = {
        'platform': 'pc',
        'ss': '367701188698225489',
        'bs': '%s',
        'RNLBSERVERID': 'ded6699',
        'FastPopSessionRequestNumber': '1',
        'FPSRN': '1',
        'performance_timing': 'home',
        'RNKEY': '40859743*68067497:1190152786:3363277230:1'
    }

    def process_request(self, request, spider):
        bs = ''
        for i in range(32):
            bs += chr(random.randint(97, 122))
        _cookie = json.dumps(self.cookie) % bs
        request.cookies = json.loads(_cookie)