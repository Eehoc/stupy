#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/2/27
import requests
try:
    r=requests.get("https://item.jd.com/28254838398.html")
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")