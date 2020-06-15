#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/5/8
import requests
from bs4 import BeautifulSoup
import re
import openpyxl
from math import radians, cos, sin, asin, sqrt
import pandas as pd
import numpy as np
import json
import math
from urllib.request import urlopen, quote

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'cookie': 'global_cookie=ndhzo4i3v9myct7aqau6zp6si10k0ncoeps; __utmz=147393320.1568695301.1.1.utmcsr=shbbs.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/esf~-1/538150834_538150842.htm; __utma=147393320.1476417876.1568695301.1568695301.1568771948.2; __utmc=147393320; Captcha=434D58793841766F7637624862786B682B684D4B454431767946477634343578436B6978474361474C45335739576D5139355553557463676C6150554F45377962612B456F624974536F383D; newhouse_user_guid=35B671E8-BF35-888C-AC78-ED09FB6489C8; newhouse_chat_guid=3262F18D-7EFB-AE4D-CC6E-D47888369019; g_sourcepage=esf_xq%5Elb_pc; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; unique_cookie=U_7eu0ocfmua6k7nyn858kd6mb727k0omb896*20; __utmb=147393320.60.10.1568771948'
}

'''第一步：爬取小区信息'''
def export_communityInfo(xiaoquInfo_dict):
    '''导出小区信息'''
    with open('浦东地区小区信息.txt', 'a', encoding='utf-8') as file:
        file.write('||'.join(xiaoquInfo_dict.values()))
        file.write('\n')

def get_true_url(old_url):
    '''获得正确的url'''
    # print(old_url)
    r = requests.get(url=old_url, headers=headers)
    if r'<title>跳转...</title>' in r.text:
        soup = BeautifulSoup(r.text, 'lxml')
        new_url = soup.find(name='a', attrs={'class': 'btn-redir'}).attrs['href']
        return new_url
    return old_url

# print(get_true_url('https://liananxilu35nong.fang.com'))

def get_region_dict():
    '''获得浦东地区不同区域的url和名称，以字典形式输出'''
    url = r"https://sh.esf.fang.com/housing/25__0_0_0_0_1_0_0_0/"
    true_url = get_true_url(url)
    r = requests.get(url=true_url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    a = soup.find(name='p', attrs={'id': 'shangQuancontain', 'class': 'contain'})
    pudong_dict = {}
    for i in a.find_all(name='a'):
        if i.string != '不限':
            pudong_dict[i.string] = r"https://sh.esf.fang.com" + i.attrs['href']
    return pudong_dict

def get_region_url(old_url):
    '''获得这个区域的其它page_url'''
    # url = r'https://sh.esf.fang.com/housing/25_1646_0_0_0_0_1_0_0_0/'
    true_url = get_true_url(old_url)
    r = requests.get(url=true_url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    page_url = soup.find(name='div', attrs={'class': 'fanye gray6'})
    page_url_list = []
    page_url_list.append(old_url)
    for j in page_url.find_all(name='a'):
        if 'href' in j.attrs:
            temp_url = r'https://sh.esf.fang.com/' + j.attrs['href'][1:]
            page_url_list.append(temp_url)
    page_urls = set(page_url_list)
    return page_urls

def get_xiaoqu_url(old_url):
    '''获得某区域某一页的小区信息和url'''
    # old_url = r'https://sh.esf.fang.com/housing/25_5920_0_0_0_0_1_0_0_0/'
    true_url = get_true_url(old_url)
    r = requests.get(url=true_url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    xiaoqu_url_dict = {}
    for i in soup.find_all(name='a', attrs={'class': 'plotTit', 'target': '_blank'}):
        xiaoqu_name = i.string
        xiaoqu_url = 'https:/' + i.attrs['href'][1:]
        xiaoqu_url_dict[xiaoqu_name] = xiaoqu_url
        # print('{}的url是{}'.format(xiaoqu_name, xiaoqu_url))
    return xiaoqu_url_dict

def get_xiaoqu_info(key, xiaoqu_name, old_url):
    '''获得小区的有用信息'''
    useful_dict = {'地区': '', '小区名称': '', '均价': '', '建筑年代': '', '建筑类型': '', '房屋总数': '', '小区位置': '', '楼栋总数': '', '物业公司': '', '开发商': ''}
    # old_url = r'https://jinqinyuan.fang.com/'
    try:
        true_url = get_true_url(old_url)
        r = requests.get(url=true_url, headers=headers)
        r.encoding = 'gb2312'
        soup = BeautifulSoup(r.text, 'lxml')
        xiaoqu_price = soup.find(name='span', attrs={'class': 'prib'}).string
        useful_dict['地区'] = key
        useful_dict['小区名称'] = xiaoqu_name
        if xiaoqu_price == '暂无均价':
            print('{}无均价数据'.format(xiaoqu_name))
            return 0
        useful_dict['均价'] = xiaoqu_price
        xiaoqu_info = soup.find(name='div', attrs={'class': 'Rinfolist'})
        for info in xiaoqu_info.select('li'):
            info = str(info)
            if re.search('''<li.*?b>(.*?)<.*?/b>(.*?)</.*?''', info):
                infos = re.search('''<li.*?b>(.*?)<.*?/b>(.*?)</.*?''', info)
                temp_key = infos.group(1)
                temp_value = infos.group(2)
                if temp_key in useful_dict.keys():
                    useful_dict[temp_key] = temp_value
        print('{}的信息已爬取'.format(xiaoqu_name))
        return useful_dict
    except:
        return 0

def xiaoqu_pachong():
    '''获取所有小区名字和链接'''
    # 首先获取浦东地区所有区域的名称和url，比如：惠南: url1
    pudong_dict = get_region_dict()
    # print(pudong_dict)
    #遍历每个分区
    for key, value in pudong_dict.items():
        print('开始{}的爬取：'.format(key))
        region_urls = get_region_url(value) #先获得每个分区的所有子url
        for page_url in region_urls:
            xiaoqu_url_dict = get_xiaoqu_url(page_url) #获得每个页面的所有小区名称和url
            for xiaoqu_name, xiaoqu_url in xiaoqu_url_dict.items():
                # print(xiaoqu_name, xiaoqu_url)
                useful_dict = get_xiaoqu_info(key, xiaoqu_name, xiaoqu_url)
                if useful_dict:
                    export_communityInfo(useful_dict)
        print('{}已爬取完毕'.format(key))
        print('--------------------------------------------------------------------')

xiaoqu_pachong()