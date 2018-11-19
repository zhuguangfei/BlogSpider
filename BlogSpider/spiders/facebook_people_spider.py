# -*- coding: utf-8 -*-
import scrapy, re, json
from scrapy import Request
from scrapy.selector import Selector
from BlogSpider.util_pools import ipPools, userAgentPools, cookiePools
from urllib.parse import quote
from BlogSpider.items import SpiderResult
from ..pipelines import SpiderResultPipeline


class FaceBookPeoPleSpider(scrapy.Spider):
    name = 'facebook_people'
    allowed_domains = ['mobile.facebook.com']
    # custom_settings = {
    #     'ITEM_PIPELINES': {'BlogSpider.pipelines.SpiderResultPipeline': 1}
    # }

    def __init__(self, **kwargs):
        # kwargs.pop('_job')
        # q = quote(kwargs.get('q'), 'DonaId J. Trump')
        q = 'trump'
        super(FaceBookPeoPleSpider, self).__init__(**kwargs)
        self.start_urls = [f'https://mobile.facebook.com/search/people/?q={q}']
        # self.start_urls = ['https://mobile.facebook.com/trump.donald.9047?refid=46']
        # self.start_urls = ['https://mobile.facebook.com/belitza.marcos.5']
        # self.start_urls = [
        #     'https://mobile.facebook.com/trump.donald.9047/friends?lst=100029290456102%3A100026051980994%3A1541037495'
        # ]
        self.cookie = {}
        # self.cookie = json.loads(paramCookie)

    def start_requests(self):
        requestList = []
        for url in self.start_urls:
            requestList.append(
                scrapy.Request(url=url, cookies=self.cookie, callback=self.parseSearch)
            )
        return requestList

    def parseSearch(self, response):
        sel = Selector(response)
        peopleLinks = sel.xpath('//td[@class="m bx"]/a/@href').extract()
        for peoplelink in peopleLinks:
            yield scrapy.Request(
                url=f'https://mobile.facebook.com/{peoplelink}',
                cookies=self.cookie,
                callback=self.parsePeoPle,
            )
        mores = sel.xpath('//div[@id="see_more_pager"]/a/@href').extract()
        for more in mores:
            yield scrapy.Request(
                url=more, cookies=self.cookie, callback=self.parseSearch
            )

    def parsePeoPle(self, response):
        # with open('f2.html', 'wb') as w:
        #     w.write(response.body)
        link = response.url.split('?')[0]
        name = link.split('/')[-1]
        with open(f'SpiderHtml/{name}.html', 'wb') as w:
            w.write(response.body)
        sel = Selector(response)
        friendsLinks = sel.xpath(
            '//div[@class="cu"]/div/div[@class="bu"]/a/@href'
        ).extract()
        i = 0
        for friendsLink in friendsLinks:
            print('+++++++++++++++++++++++++++++')
            print(friendsLink)
            print('+++++++++++++++++++++++++++++')
            yield scrapy.Request(
                url=f'https://m.facebook.com{friendsLink}',
                cookies=self.cookie,
                callback=self.parsePeoPleAllFriends,
            )
            i = i + 1
        print('------------------------')
        print(i)

    def parsePeoPleAllFriends(self, response):
        sel = Selector(response)
        friendsLinks = sel.xpath(
            '//div[@class="v ca"]/table/tbody/tr/td[@class="v s"]/a/@href'
        ).extract()
        i = 0
        for friendsLink in friendsLinks:
            yield scrapy.Request(
                url=f'https://mobile.facebook.com{friendsLink}',
                cookies=self.cookie,
                callback=self.parsePeoPle,
            )
            i = i + 1
        print('=======================')
        print(i)
