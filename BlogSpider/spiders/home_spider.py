# -*- coding:utf-8 -*-
import scrapy
from scrapy import Request


class HomeSpider(scrapy.Spider):
    name = 'home'
    allowed_domains = ['weibo.com']
    start_urls = ['https://weibo.com/']

    def parse(self, response):
        # print(response.body)
        with open('a.txt', 'w') as w:
            w.write(response.body.decode('gbk'))
