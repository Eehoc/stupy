#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/31
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Pie


def myread(path):
    df = pd.read_csv("D:\文档\爬取的内容\上市公司排行榜.csv")
    return df


def deal(df):
    t = df[["公司名称", "员工人数"]]
    print(t)
    t = t.sort_values(by="员工人数", ascending=False)
    print(t)

    return t[0:5]


def painting(t):

    (
        Pie(init_opts=opts.InitOpts(width="800px", height="500px"))
            .add(
            series_name="员工人数",
            data_pair=[list(z) for z in zip(t["公司名称"], t["员工人数"])],
            radius=["50%", "70%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
            .set_global_opts(legend_opts=opts.LegendOpts(pos_left="legft", orient="vertical"))
            .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            ),
            # label_opts=opts.LabelOpts(formatter="{b}: {c}")
        )
            .render("公司员工人数排名.html")
    )


def main():
    path = "D:\文档\爬取的内容\上市公司排行榜.csv"
    painting(deal(myread(path)))
    print("可视化成功")


main()
