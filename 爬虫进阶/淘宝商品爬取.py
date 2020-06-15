#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/3/18
import requests
import re
kv= {
    'authority': 's.taobao.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 't=4be74d2d4c55052dcc55917e838b9d01; cna=5LrwFow70noCAbddLF11HeoQ; thw=cn; cookie2=5e74214b64d7925f81cdb0c6bc5f619c; v=0; _tb_token_=e3f385beb5316; _samesite_flag_=true; sgcookie=ERRcCBdRJvErzVBDjo2xN; unb=2558504099; uc3=lg2=UIHiLt3xD8xYTw%3D%3D&id2=UU23C%2BIYvkj3tg%3D%3D&vt3=F8dBxd9maDtycMf4G%2BQ%3D&nk2=2lkotG7ZSDUHH34I92UO; csg=aa4a0fe2; lgc=%5Cu602A%5Cu5496%5Cu7537%5Cu795E%5Cu5E05%5Cu5E05%5Cu54D2i; cookie17=UU23C%2BIYvkj3tg%3D%3D; dnk=%5Cu602A%5Cu5496%5Cu7537%5Cu795E%5Cu5E05%5Cu5E05%5Cu54D2i; skt=20d53784083a755b; existShop=MTU4NDUwMDE0MQ%3D%3D; uc4=nk4=0%402GP81jOwF3I6EHHPIyBRVHDkSY3HNaLAJ9g%3D&id4=0%40U2%2Fwvx9E2RcRsfbAt6Z4PaB8LV%2Fp; tracknick=%5Cu602A%5Cu5496%5Cu7537%5Cu795E%5Cu5E05%5Cu5E05%5Cu54D2i; _cc_=VT5L2FSpdA%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=i99; _nk_=%5Cu602A%5Cu5496%5Cu7537%5Cu795E%5Cu5E05%5Cu5E05%5Cu54D2i; cookie1=ACO3Fy6J8CRLZh%2BaXcSAb5UW1IWBdjkgLQJBvlYVch4%3D; enc=n6Qy1jqK6JCxpHje7YzmlwVqjqMQL1fgk8vBuN4Bi54mcOkQmYqaRUnlh6sVytUU8Y2kxoulkHjMw26ZnM9Fcw%3D%3D; tfstk=cDYGB3_E-hSseYE4Vl_6GR13kPoda1mNCE8e8FVxZwS9T2LC_sfTYuo_6XX9IEEf.; hng=CN%7Czh-CN%7CCNY%7C156; mt=ci=2_1; JSESSIONID=007722BAF11CF2E5524A00D49A61776A; uc1=cookie14=UoTUPvXcQdHi%2Bw%3D%3D&lng=zh_CN&cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&existShop=false&cookie21=W5iHLLyFe3xm&tag=8&cookie15=UtASsssmOIJ0bQ%3D%3D&pas=0; l=dBgoh0YuQyb5AmLSBOCMqDeGWx_99IRfgulKS6wwi_5IR6YBWjQOorTHEFv6cjWAGqTB4sz4jM9tUeSYJso4ne2e4AadZqDDB; isg=BMLCu_fAKOwmXTSwuI-W99lnE8gkk8ath2fyWwzb3DXlX2PZ9CL_vQ7dC1sjDz5F',
}
def getprice_list(html):
    price_list=re.findall('"view_price":"(.*?)",',html)
    return price_list
def gettitlelist(html):
    titlelist = re.findall('"raw_title":"(.*?)",',html)
    return titlelist
def printlist(price_list,titlelist):
    print("{:5}\t{:10}\t{:^10}".format("序号","价格","商品名称"))
    n=1
    for i in range(len(price_list)):
        print("{0:^5}\t{2:<10}\t{1:{3}>10}".format(int(n),titlelist[i],price_list[i],chr(12288)))
        n+=1
def main():
    price_list=[]
    titlelist = []
    word=input("请输入需要搜索的商品：")
    depth=input("请输入需要比较的页数：")
    count=1
    bar='▉'
    for i in range(1,int(depth)+1):
        url = "https://s.taobao.com/search?q="+word+"&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s="+str(i*44)
        r = requests.get(url,headers=kv,timeout=30)
        html = r.text
        r.status_code = r.apparent_encoding
        price_list+=getprice_list(html)
        titlelist+=gettitlelist(html)
        print("\r进度:|{:<5}|{:.1%}".format('▉'*i,i/int(depth)),end="")
    print("\n")
    printlist(price_list,titlelist)
if __name__ == '__main__':
    main()