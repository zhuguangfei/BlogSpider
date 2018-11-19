# -*- coding: utf-8 -*-
import scrapy, re
from scrapy import Request
from scrapy.selector import Selector
from BlogSpider.util_pools import ipPools, userAgentPools, cookiePools
from urllib.parse import quote
from BlogSpider.items import SpiderResult


class SearchSpider(scrapy.Spider):
    name = 'weibo_search1'
    allowed_domains = ['s.weibo.com']

    def __init__(self, **kwargs):
        kwargs.pop('_job')
        q = quote(kwargs.get('q'))
        Refer = kwargs.get('Refer')
        self.uuid = kwargs.get('uuid')
        super(SearchSpider, self).__init__(**kwargs)
        self.start_urls = [f'https://s.weibo.com/weibo?q={q}&Refer={Refer}']

        self.cookie = {}

    def start_requests(self):
        requestList = []
        for url in self.start_urls:
            requestList.append(scrapy.Request(url=url, cookies=self.cookie))
        return requestList

    def parse(self, response):
        spiderResult = SpiderResult()
        sel = Selector(response)
        pages = sel.xpath('//ul[@class="s-scroll"]/li/a/@href').extract()
        if len(pages) > 0:
            for page in pages:
                url = f'https:{page}'
                yield scrapy.Request(
                    url=url, cookies=self.cookie, callback=self.pageParse
                )
        else:
            spiderResult['uuid'] = self.uuid
            spiderResult['result'] = response.body
            spiderResult['page'] = 1
            yield spiderResult

    def pageParse(self, response):
        pattern = re.compile(r'.*?page=(\d+)', flags=re.S)
        result = re.findall(pattern, response.url)
        spiderResult = SpiderResult()
        spiderResult['uuid'] = self.uuid
        spiderResult['result'] = response.body
        spiderResult['page'] = result[0]

        yield spiderResult
