#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/26
import pymongo
import pandas as pd
import numpy as np

pd.set_option('display.max_columns' ,1000)
pd.set_option('display.width' ,1000)
pd.set_option('display.max_colwidth' ,1000)


def connection_db():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["豆瓣电影排名"]
    mycol = mydb["豆瓣top250"]
    t = list(mycol.find({} ,{"_id": 0 ,'group': 1 ,'title': 1}))
    df = pd.DataFrame(t)
    return df


def get_data(df):
    group_list = list(df["group"].str.split(' '))
    group_list2 = list(set([i for j in group_list for i in j]))
    zeros_df = pd.DataFrame(np.zeros((df.shape[0] ,len(group_list2))) ,columns=group_list2)
    for i in range(len(group_list)):
        zeros_df.loc[i ,group_list[i]] = 1
    group_count = zeros_df.sum(axis=0)
    group_count = group_count.sort_values(ascending=False)
    print(group_count.values)
    return group_count


# print(group_count)
# index=group_count.index
# b=[]
# for i in range(10):
#     a=(index[i],group_count[i])
#     b.append(a)
# print(b)
# print(list(zip(group_count.index[0:10],group_count.values[0:10])))

from pyecharts import options as opts
from pyecharts.charts import Pie


def painting(group_count):
    (
        Pie()
            .add("" ,list(zip(group_count.index[0:10] ,group_count.values[0:10])))
            .set_global_opts(title_opts=opts.TitleOpts(title="电影与数量类别" ,subtitle="数据来源于豆瓣top250"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            .render("电影类别与数量.html")
    )


def main():
    painting(get_data(connection_db()))
    print("恭喜王灿大帅哥可视化成功")


main()
