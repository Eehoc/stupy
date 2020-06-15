#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/27
import requests
import re
import pprint

kv={"User-Agent":"Mozilla/5.0"}
r=requests.get("https://ncov.dxy.cn/ncovh5/view/pneumonia",headers=kv)
r.encoding="utf-8"
html=r.text
data=re.findall('<script id="getAreaStat">try { window.getAreaStat = (.*?)</script>',html)
data = eval(data[0].replace('}catch(e){}',''))
citys=[data[j]['provinceShortName'] for j in range(34)]
number=[data[j]['confirmedCount'] for j in range(34)]

from pyecharts import options as opts
from pyecharts.charts import Map

#
# c = (
#     Map()
#     .add("累计确诊", [list(z) for z in zip(citys, number)], "china")
#     .set_global_opts(title_opts=opts.TitleOpts(title="实时地图"))
#     .render("新型冠状病毒地图.html")
# )


c = (
    Map()
    .add("累计确诊", [list(z) for z in zip(citys, number)], "china",is_map_symbol_show = False)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="实时地图"),
        visualmap_opts=opts.VisualMapOpts(max_=70000,min_=1, is_piecewise=True,pieces=[
      {"min":50000,"color": 'red'},
      {"min":1000, "max": 4999},
    {"min": 500, "max": 999},
      {"min": 100, "max": 499},
      {"min": 10, "max": 99},
      {"min": 1, "max": 9, },
      {"value": 123, "label": '123（自定义特殊颜色）', "color": 'grey'},
      {"max": 5,"color": 'grey'}]),
    )
    .render("新型冠状病毒地图.html")
)
print("可视化成功")