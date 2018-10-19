# -*- coding:utf-8 -*-
import scrapy


class ProxySpider(scrapy.Spider):
    name = 'proxy'
    allowed_domains = ['www.89ip.cn']
    start_urls = ['http://www.89ip.cn/']

    def parse(self, response):
        with open('proxy.txt', 'w', encoding='utf-8') as w:
            for tr in response.xpath('//tbody/tr'):
                w.write(
                    '\t'.join(map(lambda x: x.strip(), tr.xpath('td/text()').extract()))
                )
                w.write('\n')

