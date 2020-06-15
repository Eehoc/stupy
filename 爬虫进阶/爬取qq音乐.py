#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：王灿 time:2020/3/13
import requests
import json
import os
import time
import tkinter as tk
from tkinter import *
from tkinter import END


class QQmusic:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 '}
        self.sl = []
        self.musicList = []

    # 获取页面
    def getPage(self,url,headers):
        res = requests.get(url,headers = headers)
        res.encoding = 'utf-8'
        return res

    # 获取音乐songmid
    def getSongmid(self):
        num =int(input("请输入获取数目："))
        # num = 20
        global name
        name =input("请输入歌手或歌曲名：")
        # name = '张学友'
        url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?p=1&n=%d&w=%s'%(num,name)
        # 搜索音乐
        res = self.getPage(url,headers=self.headers)
        html = res.text
        html = html[9:]
        html = html[:-1]
        # 获取songmid
        js = json.loads(html)
        songlist = js['data']['song']['list']
        for song in songlist:
            print(song)
            songmid = song['songmid']
            name = song['songname']
            self.sl.append((name,songmid))
            print('获取成功songmid')


    #获取音乐资源
    def getVkey(self):
        guid = 2255109952
        uin = 5066
        for s in self.sl:
            print('开始获取资源')
            # 获取vkey,purl
            name = s[0]
            songmid = s[1]
            keyUrl = 'https://u.y.qq.com/cgi-bin/musicu.fcg?&data={"req":{"param":{"guid":" %s"}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"%s","songmid":["%s"],"uin":"%s"}},"comm":{"uin":%s}}'%(guid,guid,songmid,uin,uin)
            time.sleep(1)
            res = self.getPage(keyUrl,headers=self.headers)
            html = res.text
            keyjs = json.loads(html)
            purl = keyjs['req_0']['data']['midurlinfo'][0]['purl']
            # 拼凑资源url
            url = 'http://dl.stream.qqmusic.qq.com/' + purl
            self.musicList.append((name,url))
            print('资源地址获取成功')

    #   下载音乐
    def downloadMusic(self):
        dir_name="D:/王灿大帅哥爬取的网络音乐/"+name
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        for m in self.musicList:
            time.sleep(1)
            url = m[1]
            res = self.getPage(url,headers=self.headers)
            music = res.content
            with open(dir_name+"/"+m[0] + '.mp3', 'wb') as f:
                f.write(music)
                print('爬取成功')




QQ = QQmusic()
QQ.getSongmid()
QQ.getVkey()
QQ.downloadMusic()




