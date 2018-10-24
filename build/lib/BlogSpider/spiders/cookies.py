# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest
import os
from scrapy.http.cookies import CookieJar
import requests
import re
import json
import urllib
import base64
import binascii
import rsa

cookie_jar = CookieJar()


def env():
    if os.path.exists('.env'):
        with open('.env', 'r') as r:
            users = []
            for line in r.read().split('\n'):
                line = line.split(' ')
                user = dict()
                user['username'] = line[0]
                user['password'] = line[1]
                users.append(user)
            return users
    else:
        print('账号文件不存在')
        return None


class CookiesSpider(scrapy.Spider):
    name = 'cookie'
    start_urls = ['https://login.sina.com.cn/sso/login.php?client=ssologin.js']

    def get_su(self, user_name):
        user_name = urllib.parse.quote(user_name)
        return base64.encodestring(user_name)[:-1]

    def get_sp_rsa(self, password, pubkey, servertime, nonce):
        key = rsa.PublicKey(int(pubkey, 16), 65537)
        message = '\t'.join([str(servertime), str(nonce)]) + '\n' + password
        encropy_pwd = rsa.encrypt(message, key)
        return binascii.b2a_hex(encropy_pwd)

    def get_prelogin_date(self):
        prelogin_url = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js'
        post_ori_test = requests.get(prelogin_url).text
        json_date = re.search(r'\((.*?)\)', post_ori_test).group(1)
        json_date = json.loads(json_date)
        prelogin_data = dict(json_date)
        for key, value in prelogin_data.items():
            prelogin_data[key] = str(value)
        return prelogin_data

    def start_requests(self):
        login_url = 'http://passport.weibo.com/wbsso/login'
        users = env()
        if users:
            for user in users:
                username = user.get('username')
                password = user.get('password')
                return [
                    scrapy.http.FormRequest(
                        url=login_url,
                        formdata={'username': username, 'password': password},
                        callback=self.get_cookie,
                    )
                ]

    def get_cookie(self, response):
        cookie_jar.extract_cookies(response, response.request)
        with open('cookie.txt', 'w') as w:
            for cookie in cookie_jar:
                w.write(str(cookie) + '\n')
        print('=============')
        print(response.url)
        print(response.body)
        print(response.headers)


if __name__ == '__main__':
    env()
