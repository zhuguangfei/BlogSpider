# -*- coding: utf8 -*-
import requests

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "SINAGLOBAL=8799106871748.773.1522035051635; _s_tentry=-; Apache=6487313550452.507.1538111417825; ULV=1538111417840:8:2:1:6487313550452.507.1538111417825:1536132862809; YF-Ugrow-G0=169004153682ef91866609488943c77f; YF-V5-G0=2a21d421b35f7075ad5265885eabb1e4; YF-Page-G0=a1c00fe9e544064d664e61096bd4d187; login_sid_t=87904fbb2938efd3063a31bd49977843; wb_view_log=1920*10801; wb_view_log_6777302762=1920*10801; wb_view_log_6573581494=1920*10801; appkey=; WBtopGlobal_register_version=9744cb1b8d390b27; WBStorage=e8781eb7dee3fd7f|undefined; SCF=AowHr_zge6tslHhoJW0Hb2521LQOrM9Wh9ec-sUwywvL7Tw1xAUNYroTtRq5c87hihU69Act10-teVHvP16h8q4.; SUHB=0HTR1BBNKYH5SG; un=13552755384; SUB=_2AkMslSZ-dcPxrAVUn_sQxGrmZYlH-jyfQE-IAn7uJhMyAxgv7n8BqSVutBF-XEMQybSfHuuflCJpXKWYAyTHpVS4; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9WFYF3eJlXxjg60nSbjicsBe5JpVF020SK-ES0-fe0nX; cross_origin_proto=SSL; UOR=www.pythontip.com,widget.weibo.com,login.sina.com.cn",
    "Host": "weibo.com",
    "Pragma": "no-cache",
    # 'Referer': "https://d.weibo.com/623751_1",
    # "Referer": "https://d.weibo.com/102803_ctg1_4288_-_ctg1_4288?from=faxian_hot&mod=fenlei",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.6 Safari/537.36",
}
rps = requests.get(url='https://weibo.com/', headers=headers)
with open('index.txt', 'w', encoding='utf-8') as w:
    w.write(rps.text)

