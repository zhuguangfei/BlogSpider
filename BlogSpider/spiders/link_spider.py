# -*- coding:utf-8 -*-
import scrapy
from scrapy import Request
from BlogSpider.util_pools import ipPools, userAgentPools, cookiePools
from bs4 import BeautifulSoup
import re


class HomeSpider(scrapy.Spider):
    name = 'link'
    allowed_domains = ['d.weibo.com']
    start_urls = ['https://d.weibo.com']

    def start_requests(self):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch, br",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Host": "d.weibo.com",
            "pragma": "no-cache",
            # "proxy": "47.105.121.78:80",
            "User-Agent": userAgentPools(),
        }
        cookie = {}
        requestList = []
        for url in self.start_urls:
            requestList.append(scrapy.Request(url=url, meta=headers, cookies=cookie))
        return requestList

    def parse(self, response):
        subPattern = re.compile(r'\\t|\\n', flags=re.S)
        with open('navigation.txt', 'wb') as w:
            w.write(response.body)
        soup = BeautifulSoup(response.body.decode('utf-8'))
        scripts = soup.find_all('script')
        for script in scripts:
            pattern = re.compile('.*?"domid":"(.*?)"', flags=re.S)
            domid = re.search(pattern, script.string)
            if domid and domid.group(1) == 'Pl_Discover_TextList__4':
                pattern = re.compile(r'.*?"html":"(.*?)"}', flags=re.S)
                content = re.findall(pattern, script.string)
                soup = BeautifulSoup(content[0])
                lis = soup.find_all('li')
                with open('link.txt', 'w', encoding='utf-8') as w:
                    for line in lis:
                        a = line.find('a')
                        link = a['href'].replace('\\"', '').replace('\/', '/')
                        w.write(f"https://d.weibo.com{link}")
                        w.write('\n')
