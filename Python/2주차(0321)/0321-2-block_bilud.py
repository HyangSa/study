import turtle as t
import math
import time
t.speed(0)

def drawLine():
    t.penup()
    t.goto(-200,200)
    t.pendown()
    t.setx(200)
    t.write('시작',font=('',20,''))
    
    t.penup()
    t.goto(-200,-200)
    t.pendown()
    t.setx(200)
    t.write('끝',font=('',20,''))

def sq(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor('black')
    t.begin_fill()
    for i in range(0,4):
        t.forward(50)
        t.rt(90)
    t.end_fill()

def dsq(x,y):
    t.penup()
    t.goto(x,y)
    t.fillcolor('white')
    t.begin_fill()
    for i in range(0,4):
        t.forward(51)
        t.rt(90)
    t.end_fill()

##a=int(input("장축 a 입력 : "))
##b=int(input("단축 b 입력 : "))
##x=int(input("x좌표 입력 : "))
##y=int(input("y좌표 입력 : "))
drawLine()
start,count,end=200,200,-150

while True:
    if (end!=start):
        for i in range(start,end-1,-50):
            sq(0,start)
            if start!=end:
                dsq(0,start)
            start=start-50
##            print(i)
        end=end+50
        start=200
    else:
        sq(0,start)
        break
        






##sq(0,200)
##sq(0,150)
##sq(0,100)
##sq(0,50)
##sq(0,0)
##sq(0,-50)
##sq(0,-100)
##sq(0,-150)
##dsq(0,200)
