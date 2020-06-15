#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/30
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Pie
def myread(path):
    pd.set_option('display.max_columns' ,1000)
    pd.set_option('display.width' ,1000)
    pd.set_option('display.max_colwidth' ,1000)
    df=pd.read_csv("D:\文档\爬取的内容\上市公司排行榜.csv")
    return df

def deal(df):
    t=df["省份"]
    lists=list(set(t.values))
    df_zero=pd.DataFrame(np.zeros((180,len(lists))),columns=lists)
    for i in range(180):
        df_zero.loc[i,t[i]]=1
    print(df_zero)
    count=df_zero.sum(axis=0)
    city_count=count.sort_values(ascending=False)
    city_count=city_count[0:10]

    return city_count

def painting(city_count):
    c = (
        Pie()
        .add("", [list(z) for z in zip(city_count.index, city_count.values)])
        .set_global_opts(title_opts=opts.TitleOpts(title="数量排名",subtitle=""))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        .render("上市公司数量排名.html")
    )
def main():
    path = "D:\文档\爬取的内容\上市公司排行榜.csv"
    painting(deal(myread(path)))
    print("可视化成功")

main()