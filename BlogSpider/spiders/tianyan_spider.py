# -*- coding:utf-8 -*-
import scrapy
import time
from bs4 import BeautifulSoup

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": "www.tianyancha.com",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
}


class TianYanSpider(scrapy.Spider):
    name = 'tianyan'
    allowed_domains = ['www.tianyancha.com']
    start_urls = ['https://www.tianyancha.com/search/oc45?base=bj&areaCode=110101']

    def start_requests(self):

        return [
            scrapy.Request(url=start_url, headers=headers)
            for start_url in self.start_urls
        ]

    def parse(self, response):
        soup = BeautifulSoup(response.body)
        xianQu = soup.find(attrs={"tyc-event-ch": "CompanySearch.Filter.Xianqu"})
        hangYe = soup.find(attrs={"tyc-event-ch": "CompanySearch.Filter.Hangye"})
        print(xianQu)
        print(hangYe)
