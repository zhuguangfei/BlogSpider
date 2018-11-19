# -*- coding: utf-8 -*-
import scrapy, json
from scrapy import Request
from selenium import webdriver
from selenium.webdriver import remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from ..items import SpiderCookieItem
from datetime import datetime
import time


class CookiesSpider(scrapy.Spider):
    name = 'cookie'
    allowed_domains = ['cookie.org']
    start_urls = ['https://www.baidu.com']
    custom_settings = {
        'ITEM_PIPELINES': {'BlogSpider.pipelines.SpiderCookiesPipeline': 1}
    }

    def __init__(self, **kwargs):
        kwargs.pop('_job')
        self.type = kwargs.get('type', 'weibo_search')
        self.username = kwargs.get('username', 'null')
        self.passwd = kwargs.get('passwd')
        super(CookiesSpider, self).__init__(**kwargs)

    def parse(self, response):
        # ua = UserAgent().random
        chrome_options = webdriver.ChromeOptions()
        if self.type == 'weibo_search':
            driver = webdriver.Chrome(
                executable_path="E:/driver/chromedriver/chromedriver.exe",
                chrome_options=chrome_options,
            )
            driver.get('https://www.weibo.com/')
            driver.set_window_size(1280, 800)
            time.sleep(15)
            if self.username != 'null':
                driver.find_element_by_xpath('//input[@id="loginname"]').clear()
                driver.find_element_by_xpath('//input[@id="loginname"]').send_keys(
                    self.username
                )
                driver.find_element_by_xpath(
                    '//input[@name="password" and @type="password"]'
                ).clear()
                driver.find_element_by_xpath(
                    '//input[@name="password" and @type="password"]'
                ).send_keys(self.passwd)
                driver.find_elements_by_xpath('//a[@node-type="submitBtn"]')[0].click()
                time.sleep(5)
        elif self.type == 'facebook_search':
            prefs = {
                'profile.default_content_setting_values': {
                    # 也可以这样写，两种都正确
                    # 'profile.default_content_settings': {
                    # 'images': 2,  # 不加载图片
                    'javascript': 2,  # 不加载JS
                    # "User-Agent": ua,  # 更换UA
                }
            }
            chrome_options.add_experimental_option("prefs", prefs)
            driver = webdriver.Chrome(
                executable_path="E:/driver/chromedriver/chromedriver.exe",
                chrome_options=chrome_options,
            )
            driver.get('https://mobile.facebook.com/')
            driver.set_window_size(1280, 800)
            time.sleep(5)
            driver.find_element_by_xpath('//input[@id="m_login_email"]').clear()
            driver.find_element_by_xpath('//input[@id="m_login_email"]').send_keys(
                self.username
            )
            driver.find_element_by_xpath('//input[@id="m_login_password"]').clear()
            driver.find_element_by_xpath('//input[@id="m_login_password"]').send_keys(
                self.passwd
            )
            driver.find_element_by_xpath('//button[@value="登录"]').click()

        cookies = driver.get_cookies()
        cookieValue = dict()
        for cookie in cookies:
            name = cookie.get('name')
            value = cookie.get('value')
            cookieValue[name] = value
        spiderCookieItem = SpiderCookieItem()
        spiderCookieItem['type_'] = self.type
        spiderCookieItem['cookies'] = json.dumps(cookieValue, ensure_ascii=False)
        spiderCookieItem['username'] = self.username
        spiderCookieItem['createTime'] = datetime.now()
        return spiderCookieItem
