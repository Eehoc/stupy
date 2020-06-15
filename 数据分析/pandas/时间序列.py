# **--coding="utf-8"--**
# 大热天编程不如吃西瓜。
# author：热耳 time:2020/6/4
import pandas as pd
import pymongo
import numpy as np
date = pd.date_range(start="20200517", end="20200603", freq="D")
print(date)
index = pd.date_range("20200517", periods=10)
print(index)


# 用时间作为索引
df = pd.DataFrame(np.random.rand(10),index=index)
print("*"*50)
print(df)

# 将豆瓣的年份进行升采样
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["豆瓣电影排名"]
mycol = mydb["豆瓣top250"]
data = list(mycol.find({},{'_id':0,'image':0}))
t = pd.DataFrame(data)
t["time"] = pd.to_datetime(t["time"])
t.set_index(t["time"],inplace=True)
t = t.resample("M").count()
print("*"*100)
print(t)
