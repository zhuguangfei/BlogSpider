# -*- coding:utf-8 -*-
import scrapy
from scrapy import Request
from BlogSpider.util_pools import ipPools, userAgentPools, cookiePools
from bs4 import BeautifulSoup
import re


# def links():
#     with open('link.txt') as r:
#         links = r.read().split('\n')
#     return links


class HomeSpider(scrapy.Spider):
    name = 'item'
    allowed_domains = ['d.weibo.item']
    start_urls = [
        'https://d.weibo.com/102803_ctg1_1552_-_ctg1_1552_oid_8008611000000000000_name_同城?from=faxian_hot&mod=fenlei#'
    ]

    def start_requests(self):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch, br",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Host": "d.weibo.com",
            "pragma": "no-cache",
            # "proxy": ipPools(),
            "User-Agent": userAgentPools(),
        }
        cookie = {}
        requestList = []
        for url in self.start_urls:
            print(url)
            requestList.append(scrapy.Request(url=url, meta=headers, cookies=cookie))
            break
        return requestList

    def parse(self, response):
        name = response.url.split('/')[-1].split('-')[0]
        with open(f'{name}.txt', 'wb') as w:
            w.write(response.body)

