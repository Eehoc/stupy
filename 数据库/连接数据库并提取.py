#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/14
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["豆瓣电影排名"]
mycol=mydb["豆瓣top250"]
for top in mycol.find({},{'_id':0,'image':0}):
    print(top)