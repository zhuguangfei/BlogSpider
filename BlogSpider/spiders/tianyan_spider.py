# -*- coding:utf-8 -*-
import scrapy

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": "www.tianyancha.com",
    "Pragma": "no-cache",
    "Referer": "https://ww.tianyancha.com/search",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
}


def parseCookie():
    cookie = dict()
    cookieStr = 'jsid=SEM-BAIDU-CG-SY-000330; TYCID=ab30714079aa11e88feae52895c72a51; undefined=ab30714079aa11e88feae52895c72a51; ssuid=7433374020; _ga=GA1.2.1291040311.1535006407; aliyungf_tc=AQAAAMytphaWYAMAwmfIfG7sdkxqUX25; csrfToken=IqFb-NTH4qyaGoQLyZLHTU11; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1542590207; _gid=GA1.2.1901409875.1542590207; RTYCID=f62c7dee46f546d5a68a3d16b15d0761; CT_TYCID=ebf0091db9334cee96f2ab379d8e7cef; cloud_token=6c01d61f860549f88eb36ee2eb52c33e; bannerFlag=true; token=8b5ca719a4e84502ad89d4912e8dbabd; _utm=b9b201408e734b64bf14e2755143a929; tyc-user-info=%257B%2522myQuestionCount%2522%253A%25220%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%252278%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzU1Mjc1NTM4NCIsImlhdCI6MTU0MjU5MzEyMSwiZXhwIjoxNTU4MTQ1MTIxfQ.9-pM0eUv_MmZDIl6yWoc6t68F4ZzJbhYpgH5A4Aj7nIoPdu5Bg1vWnMUJTzyNloBYHTfVBoYjnBTZPZWs-qqQA%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213552755384%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzU1Mjc1NTM4NCIsImlhdCI6MTU0MjU5MzEyMSwiZXhwIjoxNTU4MTQ1MTIxfQ.9-pM0eUv_MmZDIl6yWoc6t68F4ZzJbhYpgH5A4Aj7nIoPdu5Bg1vWnMUJTzyNloBYHTfVBoYjnBTZPZWs-qqQA; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1542596385'
    cookies = cookieStr.split(';')
    for ckie in cookies:
        ck = ckie.split('=')
        cookie[ck[0]] = ck[1]
    return cookie


class TianYanSpider(scrapy.Spider):
    name = 'tianyan'
    allowed_domains = ['www.tianyancha.com']
    start_urls = ['https://www.tianyancha.com/search']

    def __init__(self, **kwargs):
        # self.cookie = parseCookie()
        self.cookie = {}

    def start_requests(self):
        return [
            scrapy.Request(url=start_url, headers=headers)
            for start_url in self.start_urls
        ]

    def parse(self, response):
        with open('tianyan1.html', 'wb') as w:
            w.write(response.body)
