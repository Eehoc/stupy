#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/3/13
import requests
import re
import os
import time
kv={"User-Agent":"Mozilla/5.0"}
url = "https://www.ximalaya.com/youshengshu/12576446/"
r = requests.get(url,headers=kv)
html = r.text
hrefs = re.findall("<a title=.*? href=(.*?)>",html)
print(len(hrefs))
ids = []
for href in hrefs[2:32]:
    i = eval(href).strip().split("/")[-1]
    ids.append(i)
print(ids)
n=1
for i in ids:
    url="https://www.ximalaya.com/revision/play/v1/audio?id="+ i  +"&ptype=1"
    r=requests.get(url,headers=kv)
    data = r.json()
    media_url = data["data"]["src"]
    print(data["data"]["src"])
    print("*"*50)
    dir_name = "D:/6544"
    r=requests.get(media_url)
    f=open(dir_name+"/"+str(n)+".mp4","wb")
    f.write(r.content)
    f.close()
    n+=1
    print("爬取成功")