#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/31
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Funnel


def myread(path):
    df = pd.read_csv("D:\文档\爬取的内容\上市公司排行榜.csv")
    return df


def deal(df):
    t = df["城市"]
    lists = list(set(t.values))
    df_zero = pd.DataFrame(np.zeros((180,len(lists))),columns=lists)
    for i in range(180):
        df_zero.loc[i, t[i]]=1
    count = df_zero.sum(axis=0)
    print("/"*100)
    print(pd.value_counts(t.values))
    city_count = count.sort_values(ascending=False)
    city_count = city_count[0:10]
    return city_count


def painting(t):
    print(t)
    c = (
        Funnel()
        .add(
            "所在地",
            [list(z) for z in zip(t.index, t.values)],
            sort_="deascending",
            label_opts=opts.LabelOpts(position="inside"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="地区",subtitle="数量排名"))
        .render("地区排名.html")
    )


def main():
    path = "D:\文档\爬取的内容\上市公司排行榜.csv"
    painting(deal(myread(path)))
    print("可视化成功")


main()
