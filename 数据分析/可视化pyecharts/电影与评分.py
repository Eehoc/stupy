#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/26
import pandas as pd
import pymongo
from pyecharts.charts import Bar
from pyecharts import options as opts

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["豆瓣电影排名"]
mycol = mydb["豆瓣top250"]
data = list(mycol.find({}, {'_id': 0, 'image': 0}))
t = pd.DataFrame(data)
t2 = t.sort_values(by="score", ascending=False).iloc[0:10, :]
print(t2)
title_list = t2["title"].tolist()
score_list = t2["score"].tolist()

# 不习惯链式调用的开发者依旧可以单独调用方法
bar = Bar()
bar.add_xaxis(title_list)
bar.add_yaxis("评分", score_list)
bar.set_global_opts(title_opts=opts.TitleOpts(title="电影与评分", subtitle="数据来源于豆瓣top250"), xaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(rotate=30)))
bar.render("电影与评分.html")
print("可视化成功")
