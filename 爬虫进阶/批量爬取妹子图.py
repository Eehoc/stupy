#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/3/10
import requests
import re
import os
import time
kv={"User-Agent":"Mozilla/5.0"}
r=requests.get("https://www.vmgirls.com/3821.html",headers=kv)
html=r.text
urls=re.findall("<p><img alt=.*? src=.*? data-src=(.*?) data-nclazyload=.*? data-srcset=.*? data-sizes=.*?></p>",html)
dir_name=re.findall("<h1 class=.*?>(.*?)</h1>",html,re.S)[-1]
print(dir_name)
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
n=1
for url in urls:
    time.sleep(1)
    print(url)
    try:
        r = requests.get(eval(url),headers=kv)
        with open(dir_name + "/" + str(n) + ".jpg","wb") as f:
            f.write(r.content)
            f.close()
            n += 1
            print("爬取成功")
    except:
        print("爬取失败")
        continue

