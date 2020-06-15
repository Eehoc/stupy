#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/2/11
from random import *
from python基础.装饰器 import 装饰器函数
@装饰器函数
def main():
    程序主要内容()
    m,n,k=获得相应参数()
    s_m,s_n,w,c=多次比赛模拟(m,n,k)
    输出获胜概率(s_m,s_n,w,c)
def 程序主要内容():
    print("此程序为羽毛球竞技模拟")
    print("规则如下：")
    print("1.由任意一方先发球,输了则交换球权")
    print("2.双方只加分不减分")
    print("3.首先得到15分的获得胜利")
def 获得相应参数():
    m=eval(input("请输入球员m一个回合获胜的概率:"))
    n=eval(input("请输入球员n一个回合获胜的概率:"))
    k=eval(input("请输入比赛次数:"))
    return m,n,k
def 多次比赛模拟(m,n,k):
    s_m=0
    s_n=0
    for i in range(k):
        a=一次比赛模拟(m,n)
        if a==1:
            s_m+=1
        else:
            s_n+=1
    w=s_m/k
    c=s_n/k
    return s_m,s_n,w,c
def 一次比赛模拟(m,n):
    m1=0
    n1=0
    qq="m"
    while m1<15 and n1<15:
        if qq=="m":
            if random()<m:
                m1+=1
            else:
                n1+=1
                qq="n"
        else:
            if random()<n:
                n1+=1
            else:
                m1+=1
                qq="m"
    if m1==15:
        a=1
    else:
        a=0
    return a
def 输出获胜概率(s_m,s_n,w,c):
    print("\nm球员的获胜次数:",s_m)
    print("n球员获胜的次数:",s_n)
    print("m球员获胜的概率:",w)
    print("n球员获胜的概率:",c)
if __name__ == '__main__':
    main()





