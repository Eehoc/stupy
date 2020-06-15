#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/25
import pandas as pd
import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["豆瓣电影排名"]
mycol=mydb["豆瓣top250"]
data=list(mycol.find({},{'_id':0,'image':0}))
t=pd.DataFrame(data)
print(t)
print(t.loc[:,["title","group"]])    #取多列
print(t.loc[[0,1]])   #取多行
print(t.loc[[0,1],["title","group"]])   #取多行多列
print(t.loc[0:4])      #取连续的多行
