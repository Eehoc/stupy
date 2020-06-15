#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/3/12
import requests
import os
import re
import time
kv={"User-Agent":"Mozilla/5.0"}
url="http://www.netbian.com/"
r=requests.get(url,headers=kv)
html=r.text
list=re.findall("<img src=(.*?) a",html,re.S)
print(list)
n=1
dir_name="pic/"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
for url in list:
    time.sleep(1)
    print(url)
    try:
        pic=requests.get(eval(url),headers=kv)
    except:
        print("下载失败")
        continue
    string=dir_name+str(n)+".jpg"
    f=open(string,"wb")
    f.write(pic.content)
    f.close()
    print("爬取成功")
    n+=1