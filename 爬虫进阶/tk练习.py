#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/4/11
from tkinter import *

def GUI():
    #创建界面
    root=Tk()
    #选定标题
    root.title("网易云音乐爬取")
    #确定大小
    root.geometry("560x450")
    # 创建定位标签
    label=Label(root,text="请输入下载的歌曲：",font=("行楷",20)).grid()
    entrhkjy=Entry(root,font=("行楷",20)).grid(row=0,column=1)
    listbox=Listbox(root,font=("行楷",20),width=40,height=10).grid(row=1,columnspan=2)
    a=Button(root,text="开始下载",font=("行楷",20)).grid(row=2,column=0)
    b=Button(root,text="退出程序",font=("行楷",20),command=root.quit).grid(row=2,column=1)
    #消息循环
    root.mainloop()
def get_id():
    name="你最近还好吗"
    url="https://music.163.com/#/search/m/?s={}&type=1".format(name)
get_id()

