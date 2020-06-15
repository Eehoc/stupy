"""1.打开文件，提取单词至列表当中
2.建立字典，将单词移入字典当中
3.字典不能进行排序，故建立列表，将数据移入列表当中
4.排序后输出前十个高频词汇
5.用turtle库进行绘制柱状图"""
import turtle
count = 10
yScale = 20
xScale = 50

def wj():  # 定义文件函数
    f = open("D:\\自我介绍.txt","r")
    a = f.read()
    a.lower()
    for ch in ".,!?#:":
        a.replace(ch," ")
    print("输出文本模式：",a)
    a.strip()
    b = a.split()
    print("输出列表模式：",b)
    c = {}
    for i in b:
        c[i] = c.get(i,0) + 1
    print("输出字典模式：",c)
    d = []
    for k in c.items():
        d.append(k)
    print("输出列表中元组模式：",d)
    d.sort(key=lambda x: x[-1],reverse=True)
    print("排序之后的列表元组模式：",d)
    for i in range(10):
        m,n = d[i]
        print("{0:<10}{1:>5}".format(m,n))
    return d


a=wj()
data = []  # y的数组
words = []  # x的数组
for i in range(10):
    m,n = a[i]
    data.append(n)
    words.append(m)
print(data)
print(words)

def ht():
    turtle.title("词频结果柱状图")
    turtle.setup(900,750,0,0)
    turtle.pencolor("red")
    turtle.speed(5)
    turtle.penup()
    turtle.fd(100)
    turtle.pendown()

    drawtjt()


# 定义绘制线段函数
def drawline(x1,y1,x2,y2):
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.goto(x2,y2)


# 定义输出文字函数
def drawtext(x,y,text):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.write(text)

# 绘制一个柱体的函数
def drawygzt(x,y):
    # 放大倍数显示
    x = x * xScale
    y = y * yScale
    drawline(x - 10,0,x - 10,y)
    drawline(x - 10,y,x + 10,y)
    drawline(x+10,y,x+10,0)
    drawline(x+10,0,x-10,0)


def drawdgzt():   #绘制多个柱体
    for i in range(count):
        drawygzt(i+1,data[i])

def drawtjt():
    # 绘制x，y轴
    drawline(0,0,650,0)
    drawline(0,300,0,0)
    drawdgzt()
    for x in range(count):
        x=x+1
        drawtext(x*xScale-4,-20,(words[x-1]))
        drawtext(x*xScale-4,data[x-1]*yScale+10,data[x-1])

def main():
    wj()
    ht()
main()
turtle.done