#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/18
import requests
import re
import pymongo
def parse(html):
    items=re.findall(r'<em class="">(.*?)</em>.*?<img width="100" alt=".*?" src="(.*?)" class="">.*?'
                     r'class="title">(.*?)</span>.*?class="other">(.*?)</span>.*?<p class="">(.*?)<br>(.*? )</p>.*?'
                     r'<span class="(.*?)"></span>.*?<span class="rating_num" property="v:average">(.*?)</span>.*?<span>(.*?)人评价</span>',html,re.S)
    for item in items:
        yield {
            "index":item[0],
            "image":item[1],
            "title":item[2],
            "time":item[5].strip().split("&nbsp;/&nbsp;")[0],
            "country":item[5].strip().split("&nbsp;/&nbsp;")[1],
            "group":item[5].strip().split("&nbsp;/&nbsp;")[-1],
            "actor":item[4].strip().split()[1],
            "score":item[-2],
            "grade":item[-3],
            "people":item[-1]
    }
def main():
    top=[]
    kv = {"User-Agent": "Mozilla/5.0"}
    for i in range(0,10):
        url="https://movie.douban.com/top250?start={}&filter=".format(i*25)
        r = requests.get(url,headers=kv)
        html = r.text
        for i in parse(html):
            print(i)
            top.append(i)
    mongodb(top)
    print("导入成功")
def mongodb(top):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["豆瓣电影排名"]   #创建数据库
    mycol = mydb["豆瓣top250"]      #创建集合
    x=mycol.insert_many(top)       #插入文档
    print(x.inserted_ids)

main()


