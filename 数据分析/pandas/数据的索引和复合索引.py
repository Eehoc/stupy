# **--coding="utf-8"--**
# 大热天编程不如吃西瓜。
# author：热耳 time:2020/6/3
import pandas as pd
import pymongo
mycilent=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=mycilent["豆瓣电影排名"]
mycol=mydb["豆瓣top250"]
data=mycol.find({},{"_id":0,"image":0})
df=pd.DataFrame(data)
print(df.info())
grouped=df.groupby(by=["grade","score"]).count()["title"]
print(grouped.index)