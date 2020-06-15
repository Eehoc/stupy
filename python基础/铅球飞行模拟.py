#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/2/12
from math import *
def main():
    基本功能()
    h,v,a,t=输入参数()
    x=处理内容(h,v,a,t)
    输出结果(x)
def 基本功能():
    print("此项目为铅球飞行模拟\n输出铅球的飞行距离")
def 输入参数():
    h=eval(input("请输入铅球初始高度："))
    v=eval(input("请输入铅球初始速度："))
    a=eval(input("请输入铅球初始角度："))
    t=eval(input("请输入一个时间间隔："))
    return h,v,a,t
def 处理内容(h,v,a,t):
    g=9.8
    x=0
    p=radians(a)
    vx0=v*cos(p)
    vy0=v*sin(p)
    y=h
    while y>=0:
        x+=vx0*t
        vy=vy0-g*t
        y=h+t*(vy0+vy)/2
        vy0=vy
    return x
def 输出结果(x):
    print("飞行距离：",x)
if __name__ == '__main__':
    main()



