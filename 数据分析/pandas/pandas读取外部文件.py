#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/24
import pandas as pd
import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["豆瓣电影排名"]
mycol=mydb["豆瓣top250"]
data=list(mycol.find({},{'_id':0,'image':0}))
t=pd.DataFrame(data)
print(t)
t2=t.sort_values(by="score",ascending=False)
print(t2.loc[0:10,["title","score"]])
