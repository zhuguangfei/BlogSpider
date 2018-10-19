# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

browser = webdriver.Chrome(executable_path="E:/driver/chromedriver/chromedriver.exe")
browser.get('https://weibo.com/login')
time.sleep(10)
# browser.find_element_by_link_text('登录').click()


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


users = env()

browser.set_window_size(1280, 800)
browser.find_elements_by_xpath('//input[@name="username"]')[0].clear()
browser.find_elements_by_xpath('//input[@name="username"]')[0].send_keys(
    users[0].get('username')
)
browser.find_elements_by_xpath('//input[@name="password"]')[0].clear()
browser.find_elements_by_xpath('//input[@name="password"]')[0].send_keys(
    users[0].get('password')
)
browser.find_element_by_xpath('//a[@node-type="submitBtn"]').click()
print(browser.get_cookies())
