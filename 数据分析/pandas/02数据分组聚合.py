# **--coding="utf-8"--**
# 大热天编程不如吃西瓜。
# author：热耳 time:2020/6/3
import pymongo
import pandas as pd
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["豆瓣电影排名"]
mycol=mydb["豆瓣top250"]
data=mycol.find({},{"_id":0,"image":0})
df=pd.DataFrame(data)


print(df.info())
grouped=df["country"].groupby(by=[df["grade"],df["score"]]).count()
print(grouped)
print("--"*50)
print(df.groupby(by=["grade","score"]).count()["country"])
print("*"*100)

# 将grouped转化为DataFrame

grouped=df[["country"]].groupby(by=[df["grade"],df["score"]]).count()
print(grouped)

