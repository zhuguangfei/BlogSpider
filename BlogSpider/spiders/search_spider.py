# -*- coding: utf-8 -*-
import scrapy, re
from scrapy import Request
from scrapy.selector import Selector
from BlogSpider.util_pools import ipPools, userAgentPools, cookiePools
from urllib.parse import quote
from BlogSpider.items import SpiderResult


class SearchSpider(scrapy.Spider):
    name = 'weibo_search'
    allowed_domains = ['s.weibo.com']

    def __init__(self, **kwargs):
        kwargs.pop('_job')
        q = quote(kwargs.get('q'))
        Refer = kwargs.get('Refer')
        self.uuid = kwargs.get('uuid')
        super(SearchSpider, self).__init__(**kwargs)
        self.start_urls = [f'https://s.weibo.com/weibo?q={q}&Refer={Refer}']

        self.cookie = {
            "SINAGLOBAL": "8799106871748.773.1522035051635",
            "_s_tentry": "-",
            "Apache": "6487313550452.507.1538111417825",
            "ULV": "1538111417840:8:2:1:6487313550452.507.1538111417825:1536132862809",
            "login_sid_t": "87904fbb2938efd3063a31bd49977843",
            "appkey": "",
            "SCF": "AowHr_zge6tslHhoJW0Hb2521LQOrM9Wh9ec-sUwywvL7sd3p_Gr4o1qG2d97GEki8Q-5mjGlxMRpoat0S9S-lM.",
            "SUHB": "0xnyZVNxNrCIkY",
            "un": "13552755384",
            "SUB": "_2AkMsjatJdcPxrAVUn_sQxGrmZYlH-jyfWMK_An7uJhMyAxgv7lMrqSVutBF-XGUoRSU7hrGxOnFPx8oop4gG7SVN",
            "SUBP": "0033WrSXqPxfM72wWs9jqgMF55529P9D9WFYF3eJlXxjg60nSbjicsBe5JpVF020SK-ES0-fe0nX",
            "UOR": "www.pythontip.com,widget.weibo.com,login.sina.com.cn",
            "cross_origin_proto": "SSL",
            "WBStorage": "e8781eb7dee3fd7f|undefined",
        }

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
