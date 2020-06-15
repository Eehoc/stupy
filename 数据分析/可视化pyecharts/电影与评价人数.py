#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/26
import pymongo
import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["豆瓣电影排名"]
mycol = mydb["豆瓣top250"]
data = list(mycol.find({}, {'_id': 0, 'title': 1, 'people': 1}))
t = pd.DataFrame(data)
print(t)
t2 = t.sort_values(by="people")
print(t2)
title_list = t2["title"].iloc[0:10].tolist()
people_list = t2["people"].iloc[0:10].tolist()
print(people_list)
bar = Bar()
bar.add_xaxis(title_list)
bar.add_yaxis("评价人数", people_list)
bar.set_global_opts(title_opts=opts.TitleOpts(title="电影与评价人数", subtitle="数据来源于豆瓣top250"), xaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(rotate=30)))
bar.render("电影与评价人数.html")
print("可视化成功")

