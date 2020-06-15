#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/2/29-3/10
import requests
from bs4 import BeautifulSoup
import bs4
def getHTMLtext(url):
    kv={"User-Agent": "Mozilla/5.0" }
    r=requests.get(url,headers=kv)
    r.encoding=r.apparent_encoding
    demo=r.text
    soup=BeautifulSoup(demo,"html.parser")
    tag=soup.tbody
    print("*"*80)
    return tag
def filllist(tag):
    a=[]
    for tr in tag.children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr("td")
            a.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string,tds[4].string])
    return a
def printlist(a):
    tplt="{0:^10}\t{1:{5}^10}\t{2:^10}\t{3:^10}\t{4:^10}"
    print("{0:^10}\t{1:{5}^6}\t{2:^18}\t{3:1}\t{4:^16}".format("排名","学校","地区","总分","研究生比例",chr(12288)))
    for i in a:
        print(tplt.format(i[0],i[1],i[2],i[3],i[4],chr(12288)))
def main():
    url="http://www.zuihaodaxue.com/Greater_China_Ranking2019_0.html"
    tag=getHTMLtext(url)
    a=filllist(tag)
    printlist(a)
if __name__ == '__main__':
    main()





