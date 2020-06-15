#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/3/5
import requests
kv={"User-Agent": "Mozilla/5.0"}
path="D:\\爱的飞行日记.mp3"
url="http://ip.h5.ra01.sycdn.kuwo.cn/6b6fbc2cc7064aaa3eea527b6a9bbd4a/5e605c76/resource/n2/128/35/56/707950537.mp3"
r=requests.get(url,headers=kv)
with open(path,"wb") as f:
    f.write(r.content)