#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/2/13
class stu:  # 定义一个类
    def __init__(self,name,score,points):  # 类的构造方法
        self.name = name
        self.score = float(score)
        self.points = float(points)
f=open("D:/我的作业/学生数据.txt","r",encoding="UTF-8")
f.readline()
a=[]
for line in f:
    a.append(line.strip().split("\t"))
print(a)
x=stu(a[0][0],a[0][1],a[0][2])     #实例化类
for i in range(3):
    y=stu(a[i+1][0],a[i+1][1],a[i+1][2])
    if x.points>y.points:
        x=x
    else:
        x=y
    print(x.name)