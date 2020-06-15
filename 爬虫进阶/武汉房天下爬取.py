#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/12
import time
import requests
import re
kv={"User-Agent":"Mozilla/5.0"}
url="https://wuhan.newhouse.fang.com/house/s/"
r=requests.get(url,headers=kv)
html=r.content.decode("gbk")
data=re.findall("<a title=(.*?) target=.*? href=.*?",html)
pic=re.findall("<span>(.*?)</span><em>元/㎡</em>",html)
print(data)
print(pic)
print(len(data))
