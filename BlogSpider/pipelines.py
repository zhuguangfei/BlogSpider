# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors


class BlogspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class SpiderResultPipeline(object):
    def __init__(self):
        dbargs = dict()
        self.dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)

    def process_item(self, item, spider):
        res = self.dbpool.runInteraction(self.insert_into_table, item)
        return item

    def insert_into_table(self, conn, item):
        conn.execute(
            'insert into spider_result(uuid,page,result) values(%s,%s,%s)',
            (item['uuid'], item['page'], item['result']),
        )


class SpiderParseResultPipeline(object):
    def __init__(self):
        dbargs = dict()
        self.dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)

    def process_item(self, item, spider):
        res = self.dbpool.runInteraction(self.insert_into_table, item)
        return item

    def insert_into_table(self, conn, item):
        conn.execute(
            'insert into spider_parse_result(uuid,type,url,content,nick_name) values(%s,%s,%s,%s,%s)',
            (
                item['uuid'],
                item['type_'],
                item['url'],
                item['content'],
                item['nickName'],
            ),
        )


class SpiderCookiesPipeline(object):
    def __init__(self):
        dbargs = dict()
        self.dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)

    def process_item(self, item, spider):
        res = self.dbpool.runInteraction(self.insert_into_table, item)
        return item

    def insert_into_table(self, conn, item):
        conn.execute(
            'update spider_cookies set cookies=%s,create_time=%s where username=%s and type=%s',
            (item['cookies'], item['createTime'], item['username'], item['type_']),
        )
