#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/2/13
class stu:  # 定义一个类
    def __init__(self,name,score,points):  # 类的构造方法
        self.name = name
        self.score = float(score)
        self.points = float(points)
def main():
    主要内容()
    a=输入数据()
    x=核心功能(a)
    输出内容(x)
def 主要内容():
    print("找出GPA绩点最高的学生\n并且输出他的姓名，学分，平均绩点")
def 输入数据():
    f=open("D:/我的作业/学生数据.txt","r",encoding="UTF-8")
    f.readline()
    a=[]
    for line in f:
        a.append(line.strip().split("\t"))
    return a
def 核心功能(a):
    x=stu(a[0][0],a[0][1],a[0][2])     #实例化类
    for i in [1,2,3]:
        y=stu(a[i][0],a[i][1],a[i][2])
        if x.points<y.points:
            x=y
        else:
            x=x
    return x
def 输出内容(x):
    print("最高平均绩点已查出")
    print("学生姓名为：",x.name)
    print("学生学分为：",x.score)
    print("学生平均绩点为：",x.points)

if __name__ == '__main__':
    main()