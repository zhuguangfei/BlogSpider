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
        cookie = {
            "SINAGLOBAL": "8799106871748.773.1522035051635",
            "_s_tentry": "-",
            "Apache": "6487313550452.507.1538111417825",
            "ULV": "1538111417840:8:2:1:6487313550452.507.1538111417825:1536132862809",
            "login_sid_t": "87904fbb2938efd3063a31bd49977843",
            "YF-Ugrow-G0": "8fee13afa53da91ff99fc89cc7829b07",
            "appkey": "",
            "UOR": "www.pythontip.com,widget.weibo.com,login.sina.com.cn",
            "cross_origin_proto": "SSL",
            "SCF": "AowHr_zge6tslHhoJW0Hb2521LQOrM9Wh9ec-sUwywvLojFu38bWf_HkumtZ2AvL86w0KthBxS6tZXJeYU_e_fY.",
            "SUB": "_2A252yUYqDeRhGeBL7FEU-C_IwjiIHXVVvzDirDV8PUNbmtBeLW_BkW9NRsphvRNLkkseVXb9q_fMKvA22Pr23n7n",
            "SUBP": "0033WrSXqPxfM725Ws9jqgMF55529P9D9WFYF3eJlXxjg60nSbjicsBe5JpX5K2hUgL.FoqfS0ef1h2X1KB2dJLoI7DA9c9kP0qNehn0",
            "SUHB": "0ftZbKY8KdxMJQ",
            "ALF": "1571711477",
            "un": "13552755384",
            "wvr": "6",
            "wb_view_log": "1920*10801",
        }
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

