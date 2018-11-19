# -*- coding: utf-8 -*-
import scrapy, re, json
from scrapy import Request
from scrapy.selector import Selector
from BlogSpider.util_pools import ipPools, userAgentPools, cookiePools
from urllib.parse import quote
from BlogSpider.items import SpiderResult
from ..pipelines import SpiderResultPipeline


class FaceBookSpider(scrapy.Spider):
    name = 'facebook_search'
    allowed_domains = ['mobile.facebook.com']
    custom_settings = {
        'ITEM_PIPELINES': {'BlogSpider.pipelines.SpiderResultPipeline': 1}
    }

    def __init__(self, **kwargs):
        kwargs.pop('_job')
        q = quote(kwargs.get('q'), 'Buffett')
        self.uuid = kwargs.get('uuid', 1000)
        paramCookie = kwargs.get('cookie')
        super(FaceBookSpider, self).__init__(**kwargs)
        self.start_urls = [
            f'https://mobile.facebook.com/graphsearch/str/{q}/stories-keyword/stories-public'
        ]
        self.cookie = {}
        if paramCookie:
            self.cookie = json.loads(paramCookie)

    def start_requests(self):
        requestList = []
        for url in self.start_urls:
            meta = {'page': '1'}
            requestList.append(scrapy.Request(url=url, cookies=self.cookie, meta=meta))
        return requestList

    def parse(self, response):
        spiderResult = SpiderResult()
        spiderResult['uuid'] = self.uuid
        spiderResult['result'] = response.body
        pageNumber = response.meta['page']
        if not pageNumber:
            pageNumber = 1
        spiderResult['page'] = pageNumber
        yield spiderResult

        sel = Selector(response)
        pages = sel.xpath('//div[@id="see_more_pager"]/a/@href').extract()
        if len(pages) > 0:
            for page in pages:
                meta = {'page': str(int(pageNumber) + 1)}
                yield scrapy.Request(url=page, cookies=self.cookie, meta=meta)
