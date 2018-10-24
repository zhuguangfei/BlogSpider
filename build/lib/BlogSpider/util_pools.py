# -*- coding: utf-8 -*-
from numpy import random


def ipPools():
    ip_pools = [
        {'ip': '27.208.186.192:8060'},
        {'ip': '183.151.42.105:1133'},
        {'ip': '47.105.140.72:80'},
        {'ip': '111.226.188.83:8010'},
        {'ip': '47.105.150.214:80'},
        {'ip': '103.235.253.196:8123'},
        {'ip': '114.55.236.62:3128'},
        {'ip': '124.232.133.199:3128'},
        {'ip': '47.105.121.78:80'},
        {'ip': '36.33.25.122:808'},
        {'ip': '124.205.155.152:9090'},
        {'ip': '120.234.138.102:53779'},
        {'ip': '47.105.164.158:80'},
        {'ip': '47.105.161.185:80'},
        {'ip': '106.15.42.179:33543'},
    ]
    ip = random.choice(ip_pools)
    return ip.get('ip')


def userAgentPools():
    user_agent = [
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
    ]

    ua = random.choice(user_agent)
    return ua


def cookiePools():
    cookie = {
        "SINAGLOBAL": "8799106871748.773.1522035051635",
        "_s_tentry": "-",
        "Apache": "6487313550452.507.1538111417825",
        "ULV": "1538111417840:8:2:1:6487313550452.507.1538111417825:1536132862809",
        "YF-Ugrow-G0": "169004153682ef91866609488943c77f",
        "YF-V5-G0": "2a21d421b35f7075ad5265885eabb1e4",
        "YF-Page-G0": "a1c00fe9e544064d664e61096bd4d187"
        "login_sid_t=87904fbb2938efd3063a31bd49977843",
        "appkey": "",
        "WBtopGlobal_register_version": "9744cb1b8d390b27",
        "UOR": "www.pythontip.com,widget.weibo.com,login.sina.com.cn",
        "cross_origin_proto": "SSL",
        "WBStorage": "e8781eb7dee3fd7f|undefined",
        "wb_view_log": "1920*10801",
        "SSOLoginState": "1540175477",
        "SCF": "AowHr_zge6tslHhoJW0Hb2521LQOrM9Wh9ec-sUwywvLojFu38bWf_HkumtZ2AvL86w0KthBxS6tZXJeYU_e_fY.",
        "SUB": "_2A252yUYqDeRhGeBL7FEU-C_IwjiIHXVVvzDirDV8PUNbmtBeLW_BkW9NRsphvRNLkkseVXb9q_fMKvA22Pr23n7n",
        "SUBP": "0033WrSXqPxfM725Ws9jqgMF55529P9D9WFYF3eJlXxjg60nSbjicsBe5JpX5K2hUgL.FoqfS0ef1h2X1KB2dJLoI7DA9c9kP0qNehn0",
        "SUHB": "0ftZbKY8KdxMJQ",
        "ALF": "1571711477",
        "un": "13552755384",
        "wvr": "6",
    }
    cookies = []
    cookies.append(cookie)
    cookie = random.choice(cookies)
    return cookie
