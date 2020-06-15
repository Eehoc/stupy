#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/3/12
import requests
import re
import time
import os
kv={"User-Agent":"Mozilla/5.0"}
def ids(url):
    r=requests.get(url,headers=kv)
    html=r.text
    list=re.findall(r"<a title=.*? href=(.*?)>",html)
    return list
def writefile(m):
    dir_name = "D:/鬼谷子"
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    try:
        print(m)
        r=requests.get(m,headers=kv)
        f=open(dir_name+"/"+str(n)+"集.mp4","wb")
        f.write(r.content)
        f.close()
        print("爬取成功")
    except:
        print("爬取失败")
def api(trackid):
    url = "https://www.ximalaya.com/revision/play/v1/audio?id=" + trackid + "&ptype=1"
    time.sleep(1)
    r = requests.get(url,headers=kv)
    print(type(r))
    data = r.json()
    print(data)
    m=data["data"]['src']
    return m

def main():
    global n
    n = 1
    url="https://www.ximalaya.com/youshengshu/29497459/"
    list=ids(url)
    for i in list[3:33]:
        trackid = eval(i).split("/")[-1]
        writefile(api(trackid))
        n+=1
if __name__ == '__main__':
    main()

