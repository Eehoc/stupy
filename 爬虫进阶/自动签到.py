#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/3
import requests
import time

headers = {
    'authority': 'www.zztuku.com',
    'content-length': '0',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'origin': 'https://www.zztuku.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.zztuku.com/wordpress-2689.html',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'tk_user_id=Ozxpy9; BAIDU_SSP_lcr=https://graph.qq.com/oauth2.0/show?which=Login^&display=pc^&response_type=code^&client_id=101393123^&redirect_uri=https^%^3A^%^2F^%^2Fwww.zztuku.com^%^2Foauth-callback-qq.html^&state=^&scope=get_user_info^&display=default; Hm_lvt_36d091ca4167858e40c7bf39f954e3f9=1588508889,1588508942; Hm_lpvt_36d091ca4167858e40c7bf39f954e3f9=1588508942',
}
url="https://www.zztuku.com/user-signin.html"
r=requests.post(url,headers=headers)
m=r.json()
n=time.ctime(),":",m["msg"]
try:
    with open("/home/qiandao/log.txt","a") as f:
        f.write(str(n))
        f.close()
except:
    print("签到失败")
print(n)