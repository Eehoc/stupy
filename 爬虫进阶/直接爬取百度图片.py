#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/3/17
import requests
import re
import time
import os

kv = {"User-Agent": "Mozilla/5.0"}
def urllist(url):
    time.sleep(1)
    r=requests.get(url,headers=kv)
    urls=re.findall('"thumbURL":"(.*?)",',r.text)
    return urls

def copy(url,dir_name):
    print(url)
    time.sleep(1)
    r=requests.get(url,headers=kv)
    f=open(dir_name+str(n)+".gif","wb")
    f.write(r.content)
    f.close()

def main():
    url = "https://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fme=q=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istyp2&ie=utf-8&fm=index&pos=history&word=%E8%89%BE%E5%BC%97%E6%A3%AE"
    urls=urllist(url)
    global n
    n=1
    dir_name="D:/艾弗森/"
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    for url in urls:
        copy(url,dir_name)
        n+=1
if __name__ == '__main__':
    main()