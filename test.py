import requests
from bs4 import BeautifulSoup
import re
import json
import time


def spider():
    # url='https://d.weibo.com/'
    # url = 'https://d.weibo.com/623751_1?ajaxpagelet=1&__ref=/&_t=FM_153985794565715'

    # url = 'https://d.weibo.com/102803_ctg1_4288_-_ctg1_4288?from=faxian_hot&mod=fenlei&ajaxpagelet=1&__ref=/623751_1&_t=FM_153985794565732'
    url = 'https://weibo.com/shieldmovie?refer_flag=0000015010_&from=feed&loc=nickname'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch, br",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": "SINAGLOBAL=8799106871748.773.1522035051635; _s_tentry=-; Apache=6487313550452.507.1538111417825; ULV=1538111417840:8:2:1:6487313550452.507.1538111417825:1536132862809; YF-Ugrow-G0=169004153682ef91866609488943c77f; YF-V5-G0=2a21d421b35f7075ad5265885eabb1e4; YF-Page-G0=a1c00fe9e544064d664e61096bd4d187; login_sid_t=87904fbb2938efd3063a31bd49977843; wb_view_log=1920*10801; wb_view_log_6777302762=1920*10801; wb_view_log_6573581494=1920*10801; UOR=www.pythontip.com,widget.weibo.com,login.sina.com.cn; cross_origin_proto=SSL; appkey=; WBtopGlobal_register_version=9744cb1b8d390b27; SSOLoginState=1539941577; SCF=AowHr_zge6tslHhoJW0Hb2521LQOrM9Wh9ec-sUwywvLME9EXycnJda3uUeroTs63YrW0SbHC6BaLGk66BJ2NOg.; SUB=_2A252zdSbDeRhGeBL7FEU-C_IwjiIHXVVu0FTrDV8PUNbmtBeLVXkkW9NRsphvSTi7H-Wn45ScetdH9dnsGjouofc; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFYF3eJlXxjg60nSbjicsBe5JpX5K2hUgL.FoqfS0ef1h2X1KB2dJLoI7DA9c9kP0qNehn0; SUHB=0A05ZiNxJ4Uyrh; ALF=1571477575; un=13552755384; wvr=6",
        "Host": "weibo.com",
        "Pragma": "no-cache",
        # 'Referer': "https://d.weibo.com/623751_1",
        # "Referer": "https://d.weibo.com/102803_ctg1_4288_-_ctg1_4288?from=faxian_hot&mod=fenlei",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.6 Safari/537.36",
    }
    rep = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(rep.text)
    with open('test.txt', 'w', encoding='utf-8') as w:
        w.write(soup.prettify().replace('\t\t\t', ''))


def parse():
    with open('navigation.txt', encoding='utf-8') as r:
        content = r.read()
    soup = BeautifulSoup(content)
    scripts = soup.find_all('script')
    # print(scripts[18].string)
    pattern = re.compile('.*?"domid":"(.*?)"', flags=re.S)
    domid = re.search(pattern, scripts[17].string)
    if domid:
        print(domid.group(1))
    pattern = re.compile(r'.*?"html":"(.*?)"}', flags=re.S)
    content = re.findall(pattern, scripts[17].string)
    # soup = BeautifulSoup(content[0])
    # lis = soup.find_all('li')
    # with open('link.txt', 'w', encoding='utf-8') as w:
    #     for li in lis:
    #         link = li.a['href'].replace('\\"', '').replace('\/', '/')
    #         print(link)
    #         w.write(f"https://d.weibo.com{link}")
    #         w.write('\n')


def links():
    with open('link.txt') as r:
        links = r.read().split('\n')
    return links


def spiderByInterface():
    url = 'https://d.weibo.com/p/aj/v6/mblog/mbloglist'
    params = {
        "ajwvr": 6,
        "domain": "102803_ctg1_1552_-_ctg1_1552_oid_8008611000000000000_name_同城",
        "from": "faxian_hot",
        "mod": "fenlei",
        "pagebar": 0,
        "tab": "home",
        "current_page": 100,
        "pre_page": 1,
        "page": 1,
        "pl_name": "Pl_Core_NewMixFeed__3",
        "id": "102803_ctg1_1552_-_ctg1_1552_oid_8008611000000000000_name_同城",
        "script_uri": "/102803_ctg1_1552_-_ctg1_1552_oid_8008611000000000000_name_同城",
        "feed_type": 1,
        "domain_op": "102803_ctg1_1552_-_ctg1_1552_oid_8008611000000000000_name_同城",
        "__rnd": int(time.time() * 1000),
    }
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch, br",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "SINAGLOBAL=8799106871748.773.1522035051635; _s_tentry=-; Apache=6487313550452.507.1538111417825; ULV=1538111417840:8:2:1:6487313550452.507.1538111417825:1536132862809; login_sid_t=87904fbb2938efd3063a31bd49977843; YF-Page-G0=8fee13afa53da91ff99fc89cc7829b07; appkey=; UOR=www.pythontip.com,widget.weibo.com,login.sina.com.cn; cross_origin_proto=SSL; SSOLoginState=1540175477; SCF=AowHr_zge6tslHhoJW0Hb2521LQOrM9Wh9ec-sUwywvLojFu38bWf_HkumtZ2AvL86w0KthBxS6tZXJeYU_e_fY.; SUB=_2A252yUYqDeRhGeBL7FEU-C_IwjiIHXVVvzDirDV8PUNbmtBeLW_BkW9NRsphvRNLkkseVXb9q_fMKvA22Pr23n7n; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFYF3eJlXxjg60nSbjicsBe5JpX5K2hUgL.FoqfS0ef1h2X1KB2dJLoI7DA9c9kP0qNehn0; SUHB=0ftZbKY8KdxMJQ; ALF=1571711477; un=13552755384; wvr=6; wb_view_log_6573581494=1920*10801",
        "Host": "d.weibo.com",
        "Pragma": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.6 Safari/537.36",
    }
    rsp = requests.get(url=url, params=params, headers=headers)
    print(rsp.json())


if __name__ == '__main__':
    # spider()
    # parse()
    spiderByInterface()
