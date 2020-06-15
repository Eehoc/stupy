#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/2/27
import requests
try:
    url="https://www.baidu.com/s"
    kv={"wd":"python"}
    r=requests.get(url,params=kv)
    r.raise_for_status()
    print(r.request.url)
    print(len(r.text))
except:
    print("爬取失败")