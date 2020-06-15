#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/3/13
import requests
import time
import re
import os

kv = {"User-Agent": "Mozilla/5.0"}
def trackids(url):
    r=requests.get(url,headers=kv)
    html=r.text
    hrefs=re.findall("<a title=.*? href=(.*?)>",html)
    ids=[]
    for href in hrefs[2:32]:
        ids.append(eval(href).strip().split("/")[-1])
    return ids
def api(i):
    url="https://www.ximalaya.com/revision/play/v1/audio?id="+ i +"&ptype=1"
    r=requests.get(url,headers=kv)
    data = r.json()
    media_url = data["data"]['src']
    return media_url
def writeflie(media_url):
    dir_name="D:/阴阳师-喜马拉雅"
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    print(media_url)
    time.sleep(1)
    try:
        r=requests.get(media_url,headers=kv)
        f=open(dir_name+"/"+"第"+str(n)+"集.mp4","wb")
        f.write(r.content)
        print("爬取成功")
        f.close()
    except:
        print("爬取失败")
def main():
    url="https://www.ximalaya.com/youshengshu/12576446/"
    ids=trackids(url)
    global n
    n = 1
    for i in ids:
        writeflie(api(i))
        n+=1
if __name__ == '__main__':
    main()
