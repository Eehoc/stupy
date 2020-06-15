#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/2/26
# 图书借阅管理
import datetime

# 学生信息
class Stu_Info(object):

    def __init__(self, sno, sname, key):
        self.sno = sno
        self.key = key
        self.sname = sname
    #@staticmethod
    def Lgtime(self):
        self.ltime = datetime.datetime.now()  # 借出时间
        self.ltimes = self.ltime.strftime('%Y-%m-%d %H:%M:%S')
        self.dtime = (self.ltime +
                      datetime.timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S')  # 应归还时间

    def state(self, m):
        if m == 0:
            return '未借书'
        elif m == 1:
            return '未归还'
        elif m == 2:
            return '已归还'

    def show(self):
        print("姓名：{} 学号：{} ".format(self.sname, self.sno))

    def Show_Iden_Info(self):
        global Lend_Name
        for p in Lend_Name:
            print("学生：{} \n学号：{}\n借阅书名：{}\n借阅时间：{} \n应归还时间：{} \n归还状态：{}".format(
                self.sname, self.sno, p.Book_name, self.ltimes, self.dtime, self.state(st)))

# 图书信息


class Book_Info(object):

    def Reader(self, student):  # 建立一个借阅此书的人的列表
        self.reader_list = []
        self.reader_list.append(student)
        self.number = len(self.reader_list)

    def __init__(self, name, author, publish, count, place):
        self.Book_name = name           # 书名
        self.author    = author   		# 作者
        self.publish   = publish  		# 出版社
        self.count     = count    		# 书的数量
        self.place     = place    		# 书的位置

    def Show_Seek_Book(self):
        print("《{}》 作者：{} 出版社：{} 数量：{} 位置：{}".format(self.Book_name,
                                                     self.author, self.publish, self.count, self.place))

    def Show_readers(self):
        for q in self.reader_list:
            print("借阅人：{} 借阅时间：{} 是否归还：{}".format(
                q.sname, q.ltimes, q.state(st)))

    def Show_Management_See(self):
        print("书名：{} 数量：{} 已借出：{}".format(
            self.Book_name, self.count, self.number))
        self.Show_readers()


class Operate():
    # 查看所有图书

    @staticmethod
    def StudentSee():
        print('图书馆所有书籍：')
        for book in Book_List:  # Book_List是一个存储书籍的列表，列表中每一个元素都是Book_Info的对象
            book.Show_Seek_Book()

    # 借阅图书
    @staticmethod
    def StudentBorrow():
        global n

        Lname = input("请输入借阅图书的书名:")
        for book in Book_List:
            if Lname == book.Book_name and book.count == 0:
                print("***该书已经被借出，请稍后再来！***")
            elif Lname == book.Book_name and book.count > 0:
                global i
                book.Reader(Student_List[i])  # 在借此书的人的列表中加入这个学生
                book.count -= 1  # 书库中这本书-1
                global Lend_Name  # 一个人借的所有书的列表
                Lend_Name.append(book)
                n += 1
                global st  # 借阅状态
                st = 1
                Student_List[i].Lgtime()
                print("您已成功借到{}\n".format(book.Book_name))

    # 归还图书
    @staticmethod
    def StudentGive():
        bname = input("请输入所归还的书名：")
        for book in Book_List:
            if bname == book.Book_name:
                book.count += 1
                global st
                st = 2
                print("还书成功")

    # 查看个人信息
    @staticmethod
    def StudentInfo():
        global i
        Student_List[i].Show_Iden_Info()

    # 管理员查看图书
    @staticmethod
    def Managerment_See():
        Operate.StudentSee()
        name = input("\n请输入需要查看详细借阅信息的书名:")
        for book in Book_List:
            if name == book.Book_name:
                book.Show_Management_See()
        else:
             print("未查到此图书借阅信息！")

    # 管理员增加图书
    @staticmethod
    def ManagerAdd():
        name = input('请输入书籍的名称：')
        author = input('请输入书的作者：')
        count = input('请输入书的数量：')
        publish = input('请输入图书出版社：')
        place = input('请输入书所在的楼层：')
        Book_List.append(Book_Info(name, author, publish, count, place))
        print('{}添加成功！'.format(name))
        Operate.StudentSee()

# 身份验证


class identity(object):

    @staticmethod
    def Start():
        print('-' * 50)
        answer = input('选择用户：\n 1.管理员 \n 2.学生 \n')
        if answer == '1':
            identity.ManagerIdentity()
        elif answer == '3':
            name = input('请输入您的姓名：')
            sno = input('请输入您的学号：')
            key = input('请输入您的密码：')
            ew = Stu_Info(sno, key, name)
            Student_List.append(new)
            print('***注册成功，请登陆：***')
            dentity.StudentIdentity()
        elif answer == '2':
            identity.StudentIdentity()
        else:
            print('***操作非法***')

    def ManagerIdentity():
        passwd1 = input('请输入您的密码：')
        print('-' * 50)
        if passwd1 == '123456':
            print('欢迎使用图书管理系统')
            Menu.ManagerMenu()
        else:
            print('您的密码错误！请重新输入：')
            self.ManagerIdentity()

    @classmethod
    def StudentIdentity(self):  # 学生信息的验证函数
        num = eval(input('请输入您的学号：'))
        passwd2 = eval(input('请输入您的密码：'))
        print('-' * 50)
        for s in Student_List:
            if s.sno == num and s.key == passwd2:
                global i
                i += 1
                print('欢迎使用图书管理系统')
                Menu.StudentMenu()
                return
        print('您的用户名或身份不正确！请重新输入：')
        self.StudentIdentity()


class Menu(object):
    # 定义菜单类，学生和管理员有不同的选择

    @staticmethod
    def StudentMenu():
        print('')
        while True:
            print("\n1.查看书籍 2.借阅图书 3.归还图书 4.查看个人信息 5.切换登陆 0.退出系统\n")
            Schoice = input('请选择您要进行的操作：')
            if Schoice == '1':
                Operate.StudentSee()
            elif Schoice == '2':
                Operate.StudentBorrow()
            elif Schoice == '3':
                Operate.StudentGive()
            elif Schoice == '4':
                Operate.StudentInfo()
            elif Schoice == '5':
                print('')
                print('***欢迎再次使用图书管理系统***')
                identity.Start()
            elif Schoice == '0':
                print('')
                print('***欢迎再次使用图书管理系统***')
                return 0
            else:
                print('您的输入不正确，请重新输入数字\n')

    @staticmethod
    def ManagerMenu():
        # 定义管理员选择菜单函数
        print('')
        print('1.查看书籍\n')
        print('2.增加图书\n')
        print('3.切换登陆\n')
        print('0.退出系统\n')
        while True:
            Mchoice = input('请选择您要进行的操作：')
            if Mchoice == '1':
                # 管理员查看图书部分
                Operate.Managerment_See()
            elif Mchoice == '2':
                # 管理员增加图书部分
                Operate.ManagerAdd()
            elif Mchoice == '3':
                # 退出菜单部分
                print('')
                print('***欢迎再次使用图书管理系统***')
                identity.Start()
            elif Mchoice == '0':
                print('')
                print('***欢迎再次使用图书管理系统***')
                return 0
            else:
                print('您的输入不正确，请重新输入\n')


def main():  # 测试数据
    global Book_List  # 图书馆的所有书
    global n
    n = -1
    global i  # Student_List中标识人的下标
    i = -1
    Book_List = []
    book1 = Book_List.append(
        Book_Info('Python程序设计', '董富国', '清华大学出版社', 5, '1F'))
    book2 = Book_List.append(Book_Info('数据结构', '严蔚敏', '清华大学出版社', 5, '1F'))
    book3 = Book_List.append(Book_Info('西游记', '吴承恩', '人民出版社', 4, '2F'))
    book4 = Book_List.append(
        Book_Info('爱丽丝梦游仙境', 'Lewis Carroll', '人民出版社', 5, '3F'))
    global Student_List  # 图书馆的所有注册学生信息
    Student_List = []
    s1 = Student_List.append(Stu_Info(112, 'Ammy', 123))
    s2 = Student_List.append(Stu_Info(113, 'Tom', 345))
    global Lend_Name
    Lend_Name = []

    # 设置存放一个学生借的所有书的列表

    identity.Start()
if __name__ == '__main__':
    main()

