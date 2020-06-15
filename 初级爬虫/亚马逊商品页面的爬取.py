#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/2/27
import requests
try:
    kv={"User-Agent":"Mozilla/5.0"}
    r=requests.get("https://www.amazon.cn/dp/B01LZQA8WB/ref=sr_1_4?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&keywords=dw&qid=1582774041&rnid=124355071&s=watch&sr=1-4",headers=kv)
    r.raise_for_status()
    print(r.status_code)
    print(r.encoding)
    print(r.apparent_encoding)
    print(r.request.headers)
    r.encoding=r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")

