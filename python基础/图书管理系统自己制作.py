#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/2/15

class book:
    def __init__(self,name,author,num,lc):   #创建书 类
        self.name=name
        self.author=author
        self.num=int(num)
        self.lc=lc
    def reader(self,student):
        global read
        read=[]
        read.append(student)
    def sc(self):
        global read
        print(r"借阅人：")
        for i in read:
            print(i.name)
    def state(self):
        len(read)
class stu:
    def __init__(self,name,num,mm):
        self.name=name
        self.num=int(num)
        self.mm=int(mm)

class identity:  #身份验证 类
    @staticmethod
    def start():
        print("1.学生\t2.管理员")
        m={1:"identity.yhdl()",2:"identity.manager()"}
        eval(m[eval(input("请选择："))])

    @staticmethod
    def yhdl():
        print("1.登录\t2.注册")                             #这是一个实例方法所以调用时必须出现实例
        m={1:"identity.Login()",2:"identity.register()"}
        eval(m[eval(input("请选择："))])

    @staticmethod
    def manager():
        a=eval(input("请输入工号："))
        b=eval(input("请输入管理员密码："))
        global man
        if a in man:
            if b==8520:
                menu.manage()
            else:
                print("输入管理员密码错误请核对")
                identity.manager()
        else:
            print("输入的工号有误")
            identity.manager()

    @staticmethod
    def register():
        print("-"*50)
        name=input("请输入姓名：")
        num=input("请输入学号：")
        mm=input("请输入密码：")
        stus.append(stu(name,num,mm))
        print("***注册成功***")
        identity.Login()

    @staticmethod
    def Login():
        a = eval(input("请输入学号："))
        b = eval(input("请输入密码："))
        print("-" * 50)
        for j in stus:
            global k
            k+=1
            if j.num == a:
                if j.mm == b:
                    print('欢迎使用图书管理系统')
                    menu.stu()
                else:
                    print("密码输入错误")
            else:
                continue
        else:
            print("输入错误，请核对")
            identity.Login()

# 菜单
class menu:
    @staticmethod
    def stu():
        print("1.查看书籍\n2.借阅图书\n3.归还图书\n4.查看个人信息\n5.切换登陆\n0.退出系统")
        print("-"*50)
        a=eval(input("请选择："))
        if a==1:
            operate.show()
        elif a==2:
            operate.lend()
        elif a==3:
            operate.revert()
        elif a==4:
            operate.showall()
        elif a==5:
            operate.switch()
        elif a==0:
            operate.quit()

    @staticmethod
    def manage():
        print("1.增加图书\n2.删除图书\n3.查看图书信息")
        m={1:"operate.add()",2:"operate.dell()",3:"operate.find()"}
        eval(m[eval(input("请选择"))])

#相关操作内容
class operate:
    @staticmethod
    def show():
        for i in books:
            print("书名：《{}》\n作者：{}\n数量：{}\n楼层：{}".format(i.name,i.author,i.num,i.lc))
        a=input("按任意键返回")
        print("-"*50)
        menu.stu()

    @staticmethod
    def lend():
        a=input("请输入书名：")
        for i in books:
            if i.name==a and i.num>0:
                print("书名：《{}》\n作者：{}\n数量：{}\n楼层：{}".format(i.name,i.author,i.num,i.lc))
                i.reader(stus[k])
                i.num-=1
                global stulend
                stulend.append(i)
                print("成功借出")
                print(i.state())
                a = input("按任意键返回")
                print("-" * 50)
                menu.stu()
            elif i.name==a and i.num==0:
                print("***此书已被借出***")
        else:
            print("输入错误，请核对")
            operate.lend()

    @staticmethod
    def add():
        books.append(book(input("请输入书名："),input("请输入作者："),input("请输入数量:"),input("请输入楼层:")))
        input("按任意键返回")
        menu.manage()

    @staticmethod
    def dell():
        a=input("请输入书名：")
        for i in books:
            if i.name==a:
                books.remove(i)
                input("按任意键返回")
                menu.manage()
            else:
                continue
        else:
            print("查无此书")

    @staticmethod
    def find():
        for i in books:
            print("书名：《{}》\n作者：{}\n数量：{}\n楼层：{}".format(i.name,i.author,i.num,i.lc))
            i.sc()
        input("按任意键返回")
        menu.manage()

    @staticmethod
    def revert():
        a=input("请输入书名：")
        for i in books:
            if i.name==a:
                i.num+=1
                print("***还书成功***")
        a = input("按任意键返回")
        print("-" * 50)
        menu.stu()

    @staticmethod
    def showall():
        print("姓名：{}\n学号：{}\n密码：{}".format(stus[k].name,stus[k].num,stus[k].mm))
        global stulend
        for i in stulend:
            print(i.name)
        a = input("按任意键返回")
        print("-" * 50)
        menu.stu()

    @staticmethod
    def switch():
        print("欢迎下次使用")
        print("-" * 50)
        global k
        k=-1
        identity.start()

    @staticmethod
    def quit():
        print("欢迎下次使用")
        print("-"*50)
        exit()
def main():
    global k          #登陆人的下角标
    k=-1
    global books      #存放书的列表
    books=[]
    books.append(book('戴晨为什么这么美', '王灿',"5", '1F'))
    books.append(book("戴晨的减肥计划","戴晨","6","5F"))
    books.append(book("五毛钱怎么活三天","王灿","8","6F"))
    global stus       #存放学生的列表
    stus=[]
    stus.append(stu("王灿","123456","123456"))
    stus.append(stu("戴晨","123","123"))
    global stulend   #存放一个人借的书的列表
    stulend = []
    global man       #存放工号的列表
    man=[]
    man.append(int(991224))
    man.append(int(991218))
    identity.start()
if __name__ == '__main__':
    main()