# 大热天编程不如吃西瓜
# author：热耳 time:2020/6/3
import pandas as pd
import numpy as np
import pymongo
mycilent=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=mycilent["豆瓣电影排名"]
mycol=mydb["豆瓣top250"]
data=mycol.find({},{'_id':0,'image':0})
data=pd.DataFrame(data)
df=data.groupby(by="country").count()
a=pd.get_dummies(data)
print(a)
# 进行遍历
"""
for i in df:
    print(i)
        """
# print(data[data["country"]=="德国"])

# 进行聚合
"""
print(df["title"].count())
"""
