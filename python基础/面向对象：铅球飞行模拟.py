#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/2/14
# 定义一个类
from math import *
class qq:
    def __init__(self,v,a,h):   #创建一个投射体对象
        p=radians(a)
        self.vx=v*cos(p)
        self.vy=v*sin(p)
        self.x=0
        self.y=h
    def 更新(self,t):
        while self.y>=0:
            self.x+=t*self.vx
            v1=self.vy-9.8*t
            self.y+=t*(v1+self.vy)/2
            self.vy=v1
    def 输出数据(self):
        print(self.x)
def main():
    介绍内容()
    v,a,h,t=输入数据()
    核心内容(v,a,h,t)
def 输入数据():
    v=eval(input("请输入初始速度："))
    a=eval(input("请输入初始角度："))
    h=eval(input("请输入初始高度："))
    t=eval(input("请设计时间间隔："))
    return v,a,h,t
def 介绍内容():
    print("此项目为面向对象实例\n采用类的方法来模拟铅球飞行")
def 核心内容(v,a,h,t):
    m=qq(v,a,h)    #一个对象
    m.更新(t)
    m.输出数据()

if __name__ == '__main__':
    while 1:
        main()


