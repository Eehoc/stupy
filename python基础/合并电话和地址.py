#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/2/8

def main():
# 读取文件内容
    f1=open("D:/我的作业/电话本.txt","r",encoding="UTF-8")
    f2=open("D:/我的作业/地址.txt","r",encoding="UTF-8")
    f1.readline()
    f2.readline()
    a={}
    b={}
    for line in f1:
        m1=line.strip().split()
        a[m1[0]]=m1[1]
    print(a)
    for line in f2:
        m2=line.strip().split()
        b[m2[0]]=m2[1]
    print(b)
    # 合并信息
    s="姓名\t电话\t地址\n"
    for key in a:
        if key in b.keys():
            s+="\t".join([key,a[key],b[key]])
            s+="\n"
        else:
            s+="\t".join([key,a[key],str("--------")])
            s+="\n"
    # 处理文件二中剩余的数据
    for key in b:
        if key not in a.keys():
            s+="\t".join([key,str("--------"),b[key]])
            s+="\n"

    c=[]
    c.append(s)
    print(len(c))
    # 创建一个新文件，用于放置数据
    f3=open("D:/我的作业/字典：电话地址本.txt","w")
    f3.writelines(c)
    f3.close()

    # 遍历文件，输出文件3的内容
    f4=open("D:/我的作业/字典：电话地址本.txt","r").read()
    print(f4)
    # 关闭文件
    f1.close()
    f2.close()
# 字符串中带有换行，使用writelines函数可以直接打印出来换行符，进行写入

if __name__ == '__main__':
    main()