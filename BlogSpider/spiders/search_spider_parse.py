# -*- coding: utf-8 -*-
import scrapy, re, json
from scrapy import Request
from scrapy.selector import Selector
from BlogSpider.util_pools import ipPools, userAgentPools, cookiePools
from urllib.parse import quote
from BlogSpider.items import SpiderParseResult, SpiderResult
from bs4 import BeautifulSoup


class SearchSpider(scrapy.Spider):
    name = 'weibo_search'
    allowed_domains = ['s.weibo.com']
    custom_settings = {
        'ITEM_PIPELINES': {'BlogSpider.pipelines.SpiderParseResultPipeline': 1}
    }

    def __init__(self, **kwargs):
        kwargs.pop('_job')
        q = quote(kwargs.get('q'))
        Refer = kwargs.get('Refer', 'index')
        self.uuid = kwargs.get('uuid', 1000)
        paramCookie = kwargs.get('cookie')
        super(SearchSpider, self).__init__(**kwargs)
        self.start_urls = [f'https://s.weibo.com/weibo?q={q}&Refer={Refer}']

        self.cookie = {}
        if paramCookie:
            self.cookie = json.loads(paramCookie)

    def start_requests(self):
        requestList = []
        for url in self.start_urls:
            requestList.append(scrapy.Request(url=url, cookies=self.cookie))
        return requestList

    def parse(self, response):
        sel = Selector(response)
        pages = sel.xpath('//ul[@class="s-scroll"]/li/a/@href').extract()
        if len(pages) > 0:
            for page in pages:
                url = f'https:{page}'
                yield scrapy.Request(
                    url=url, cookies=self.cookie, callback=self.pageParse
                )
        else:
            self.pageParse(response)

    def pageParse(self, response):
        soup = BeautifulSoup(response.body)
        soup = soup.find(class_='m-con-l')
        cardWraps = soup.find_all(class_="card-wrap")
        for cardWrap in cardWraps:
            if 'wrap-continuous' not in cardWrap['class']:
                avator = cardWrap.find(class_='avator')
                articles = cardWrap.find_all(class_='card-article-a')
                if avator:
                    spiderParseResult = SpiderParseResult()
                    spiderParseResult['uuid'] = self.uuid
                    avator = avator.a['href']
                    spiderParseResult['url'] = f'http:{avator}'
                    spiderParseResult['type_'] = 'post'
                    content = cardWrap.find(class_='content')
                    if content:
                        p = content.p
                        spiderParseResult['content'] = p.text.strip()
                        spiderParseResult['nickName'] = p['nick-name'].strip()
                    else:
                        spiderParseResult['content'] = None
                        spiderParseResult['nickName'] = None
                    yield spiderParseResult
                elif len(articles) > 0:
                    for article in articles:
                        spiderParseResult = SpiderParseResult()
                        spiderParseResult['uuid'] = self.uuid
                        articleLink = article.h3.a['href']
                        content = article.find(class_='content').text
                        spiderParseResult['url'] = articleLink
                        spiderParseResult['type_'] = 'article'
                        spiderParseResult['content'] = content.strip()
                        spiderParseResult['nickName'] = None
                        yield spiderParseResult
