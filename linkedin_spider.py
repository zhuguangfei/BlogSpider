# -*- coding:utf-8 -*-
import requests
import time
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from datetime import datetime
import MySQLdb

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
}


def linkedinSelenium():
    browser = webdriver.Chrome('E:\driver\chromedriver\chromedriver.exe')
    browser.get("https://www.baidu.com")
    browser.maximize_window()
    cookies = []
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.get(
        "https://www.linkedin.com/search/results/people/?facetCurrentCompany=350419"
    )
    time.sleep(3)
    while True:
        peoples = dict()
        for index in range(3):
            browser.execute_script(
                f"window.scrollTo(0, document.body.scrollHeight*{index+1}/3);"
            )
            items = browser.find_elements_by_xpath(
                '//li[@class="search-result search-result__occluded-item ember-view"]//div[@class="search-result__wrapper"]//div[@class="search-result__info pt3 pb4 ph0"]'
            )
            for item in items:
                value = list()
                name = item.find_element_by_tag_name("a").text
                company = item.find_elements_by_tag_name("p")[0].text
                region = item.find_elements_by_tag_name("p")[1].text
                name = name.split('\n')
                value.extend(name)
                value.append(company)
                value.append(region)
                peoples[name[0]] = value
        with open('fuxing.txt', 'a', encoding="utf-8") as w:
            for key, value in peoples.items():
                w.write(f"{key}\t{value[-3]}\t{value[-2]}\t{value[-1]}\n")
        nextPage = browser.find_element_by_xpath('//div[@class="next-text"]')
        if nextPage.is_displayed():
            break
        else:
            nextPage.click()
            time.sleep(2)


def linkedinCompany():
    browser = webdriver.Chrome('E:\driver\chromedriver\chromedriver.exe')
    browser.get("https://www.baidu.com")
    browser.maximize_window()
    cookies = []
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.get("https://www.linkedin.com/search/results/companies/")
    time.sleep(3)
    while True:
        peoples = dict()
        for index in range(3):
            browser.execute_script(
                f"window.scrollTo(0, document.body.scrollHeight*{index+1}/3);"
            )
            items = browser.find_elements_by_xpath(
                '//li[@class="search-result search-result__occluded-item ember-view"]//div[@class="search-result__wrapper"]//div[@class="search-result__info pt3 pb4 pr0"]'
            )
            for item in items:
                value = list()
                name = item.find_element_by_tag_name("a")
                company = item.find_elements_by_tag_name("p")[0].text
                id = name.get_attribute('href')
                value.append(name.text)
                value.append(id)
                value.append(company)
                peoples[name.text] = value
        # with open('company.txt', 'a', encoding="utf-8") as w:
        #     for key, value in peoples.items():
        #         w.write(f"{key}\t{value[-2]}\t{value[-1]}\n")
        db = MySQLdb.connect()
        cursor = db.cursor()
        for key, value in peoples.items():
            #         w.write(f"{key}\t{value[-2]}\t{value[-1]}\n")
            cursor.execute(
                '''insert into spider_linked_company(name,url,descraption) values(%s,%s,%s)''',
                [key, value[-2], value[-1]],
            )
        db.commit()
        db.close()
        print(f"保存数量：{len(peoples.items())};时间：{datetime.now()}")
        nextPage = browser.find_element_by_xpath('//div[@class="next-text"]')
        # if nextPage.is_displayed():
        #     break
        # else:
        nextPage.click()
        time.sleep(2)


if __name__ == '__main__':
    linkedinCompany()
    # linkedinSelenium()
