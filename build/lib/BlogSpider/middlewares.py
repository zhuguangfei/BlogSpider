# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from scrapy.downloadermiddlewares.cookies import CookiesMiddleware
import random


class BlogspiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class BlogspiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class IpPools(HttpProxyMiddleware):
    def __init__(self, ip=''):
        self.ip_pools = [
            {'ip': '27.208.186.192:8060'},
            {'ip': '183.151.42.105:1133'},
            {'ip': '47.105.140.72:80'},
            {'ip': '111.226.188.83:8010'},
            {'ip': '47.105.150.214:80'},
            {'ip': '103.235.253.196:8123'},
            {'ip': '114.55.236.62:3128'},
            {'ip': '124.232.133.199:3128'},
            {'ip': '47.105.121.78:80'},
            {'ip': '36.33.25.122:808'},
            {'ip': '124.205.155.152:9090'},
            {'ip': '120.234.138.102:53779'},
            {'ip': '47.105.164.158:80'},
            {'ip': '47.105.161.185:80'},
            {'ip': '106.15.42.179:33543'},
        ]

    def process_request(self, request, spider):
        ip = random.choice(self.ip_pools)
        print(f"当前IP{ip['ip']}")
        try:
            request.meta['proxy'] = f"http://{ip['ip']}"
        except Exception as e:
            print(e)


class UserAgentPools(UserAgentMiddleware):
    def __init__(self, user_agent=''):
        self.user_agent = [
            'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
        ]

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent)
        print(f'当前使用user-agent是{ua}')
        try:
            request.headers.setdefault('User-Agent', ua)
        except Exception as e:
            print(e)


class CookiePools(object):
    def __init__(self):
        cookie = {
            "SINAGLOBAL": "8799106871748.773.1522035051635",
            "_s_tentry": "-",
            "Apache": "6487313550452.507.1538111417825",
            "ULV": "1538111417840:8:2:1:6487313550452.507.1538111417825:1536132862809",
            "YF-Ugrow-G0": "169004153682ef91866609488943c77f",
            "YF-V5-G0": "2a21d421b35f7075ad5265885eabb1e4",
            "YF-Page-G0": "a1c00fe9e544064d664e61096bd4d187"
            "login_sid_t=87904fbb2938efd3063a31bd49977843",
            "appkey": "",
            "WBtopGlobal_register_version": "9744cb1b8d390b27",
            "UOR": "www.pythontip.com,widget.weibo.com,login.sina.com.cn",
            "cross_origin_proto": "SSL",
            "WBStorage": "e8781eb7dee3fd7f|undefined",
            "wb_view_log": "1920*10801",
            "SSOLoginState": "1540175477",
            "SCF": "AowHr_zge6tslHhoJW0Hb2521LQOrM9Wh9ec-sUwywvLojFu38bWf_HkumtZ2AvL86w0KthBxS6tZXJeYU_e_fY.",
            "SUB": "_2A252yUYqDeRhGeBL7FEU-C_IwjiIHXVVvzDirDV8PUNbmtBeLW_BkW9NRsphvRNLkkseVXb9q_fMKvA22Pr23n7n",
            "SUBP": "0033WrSXqPxfM725Ws9jqgMF55529P9D9WFYF3eJlXxjg60nSbjicsBe5JpX5K2hUgL.FoqfS0ef1h2X1KB2dJLoI7DA9c9kP0qNehn0",
            "SUHB": "0ftZbKY8KdxMJQ",
            "ALF": "1571711477",
            "un": "13552755384",
            "wvr": "6",
        }
        cookies = []
        cookies.append(cookie)
        self.cookies = cookies

    def process_request(self, request, spider):
        cookie = random.choice(self.cookies)
        print('当前使用cookie')
        try:
            request.cookies = cookie
        except Exception as e:
            print(e)
