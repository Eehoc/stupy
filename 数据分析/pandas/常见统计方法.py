#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/26
import pandas as pd
import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["豆瓣电影排名"]
mycol=mydb["豆瓣top250"]
data=list(mycol.find({},{'_id':0,'image':0}))
t=pd.DataFrame(data)
print(t)
print(t.loc[:,["actor","score"]])
print(t["score"].astype(float).mean())
a=t["actor"].tolist()
print(len(t["actor"].tolist()))
