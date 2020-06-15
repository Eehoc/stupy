#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/27
import pymongo
import pandas as pd
import numpy as np
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["豆瓣电影排名"]
mycol=mydb["豆瓣top250"]
data=list(mycol.find({},{'_id':0,'time':1}))
t=pd.DataFrame(data)
df=list(t["time"].str.split(" / "))
df_all=[i for j in df for i in j]
set_df=list(set(df_all))
zeros_df=pd.DataFrame(np.zeros((t.shape[0],len(set_df))),columns=set_df)
for i in range(t.shape[0]):
    zeros_df.loc[i,df[i]]=1

time_count=zeros_df.sum(axis=0)
time_count=time_count.sort_values(ascending=False)


import pyecharts.options as opts
from pyecharts.charts import Pie

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.baidu.com/examples/editor.html?c=pie-doughnut

目前无法实现的功能:

1、迷之颜色映射的问题
"""

x_data = time_count.index[0:10]
y_data = time_count.values[0:10]
data_pair = [list(z) for z in zip(x_data, y_data)]
data_pair.sort(key=lambda x: x[1])

(
    Pie(init_opts=opts.InitOpts(width="1600px", height="800px", bg_color="#2c343c"))
    .add(
        series_name="电影数量",
        data_pair=data_pair,
        rosetype="radius",
        radius="70%",
        center=["50%", "50%"],
        label_opts=opts.LabelOpts(is_show=False, position="center"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="年份电影数量",
            pos_left="center",
            pos_top="20",
            title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
        ),
        legend_opts=opts.LegendOpts(is_show=False),
    )
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ),
        label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
    )
    .render("年份电影数量.html")
)
print("可视化成功")