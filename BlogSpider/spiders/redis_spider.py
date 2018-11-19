from scrapy_redis.spiders import RedisSpider
from scrapy.selector import Selector
import scrapy
from bs4 import BeautifulSoup
from BlogSpider.items import SpiderParseResult
from urllib.parse import unquote


class MySpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""

    name = "wb"
    # 启动爬虫的命令
    redis_key = "wb:start_urls"
    custom_settings = {
        'ITEM_PIPELINES': {'BlogSpider.pipelines.SpiderParseResultPipeline': 1}
    }

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('weibo', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        url = unquote(response.url.split('&')[0])
        soup = BeautifulSoup(response.body)
        soup = soup.find(class_='m-con-l')
        cardWraps = soup.find_all(class_="card-wrap")
        for cardWrap in cardWraps:
            if 'wrap-continuous' not in cardWrap['class']:
                avator = cardWrap.find(class_='avator')
                articles = cardWrap.find_all(class_='card-article-a')
                if avator:
                    spiderParseResult = SpiderParseResult()
                    spiderParseResult['uuid'] = url
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
                        spiderParseResult['uuid'] = url
                        articleLink = article.h3.a['href']
                        content = article.find(class_='content').text
                        spiderParseResult['url'] = articleLink
                        spiderParseResult['type_'] = 'article'
                        spiderParseResult['content'] = content.strip()
                        spiderParseResult['nickName'] = None
                        yield spiderParseResult
