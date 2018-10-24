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
        cookie = {
            "SINAGLOBAL":"8799106871748.773.1522035051635",
            "_s_tentry":"-",
            "Apache":"6487313550452.507.1538111417825", 
            "ULV":"1538111417840:8:2:1:6487313550452.507.1538111417825:1536132862809",
            "login_sid_t":"87904fbb2938efd3063a31bd49977843",
            "YF-Page-G0":"8fee13afa53da91ff99fc89cc7829b07",
            "appkey":"",
            "cross_origin_proto":"SSL", 
            "UOR":"www.pythontip.com,widget.weibo.com,www.baidu.com", 
            "SCF":"AowHr_zge6tslHhoJW0Hb2521LQOrM9Wh9ec-sUwywvLibYevNUDulIH5wG0MNWIdgjOx_QqufNgdsrzgh-Ylas.", 
            "SUB":"_2A252yopUDeRhGeBL7FEU-C_IwjiIHXVVofycrDV8PUNbmtBeLWLakW9NRsphvX6Xnpl7evp-dACinvIV1ICn9OnO", 
            "SUBP":"0033WrSXqPxfM725Ws9jqgMF55529P9D9WFYF3eJlXxjg60nSbjicsBe5JpX5K2hUgL.FoqfS0ef1h2X1KB2dJLoI7DA9c9kP0qNehn0",
            "SUHB":"0Elq-q17inqgCW",
            "un":"13552755384",
            "wvr":"6",
            "wb_view_log_6573581494":"1920*10801"
        }
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
                        w.write(
                            f"https://d.weibo.com{link}"
                        )
                        w.write('\n')
