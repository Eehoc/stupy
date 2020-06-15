# **--coding="utf-8"--**
# 大热天编程不如吃西瓜。
# author：热耳 time:2020/6/9
import requests
url = "https://m10.music.126.net/20200609134518/1d620f3ddc764b1faafe0ba1585adde4/ymusic/e7d5/196e/81a4/bad7a4b07d215729" \
      "a469819928593430.mp3"
kv = {"User-Agent": "Mozilla/5.0"}
r = requests.get(url, headers=kv)
with open("E:/LUORIFEICHE.mp3", "wb") as f:
    f.write(r.content)
