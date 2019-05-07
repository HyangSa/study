import turtle as t
import math
t.speed(0)

def drawLine():
    t.penup()
    t.setx(-200)
    t.pendown()
    t.setx(200)
    t.write('x',font=('',20,''))
    
    t.penup()
    t.goto(0,200)
    t.pendown()
    t.sety(-200)
    t.write('y',font=('',20,''))


##a=int(input("장축 a 입력 : "))
##b=int(input("단축 b 입력 : "))
##x=int(input("x좌표 입력 : "))
##y=int(input("y좌표 입력 : "))
a=200
b=100
curx=100
cury=100
angle=0
drawLine()

t.penup()
t.goto(curx,cury)
t.pendown()
t.dot(a,"blue")
t.goto(curx,cury)
t.dot(b,"red")

t.penup()
##t.goto(curx,cury)
##t.left(120)
##t.forward(b/2)

x=curx+math.cos(math.radians(1))*a/2
y=curx+math.sin(math.radians(1))*b/2
t.goto(x,y)
t.pendown()



for i in range(0,360):
    x=(math.cos(math.radians(i))*a/2)
    y=(math.sin(math.radians(i))*b/2)
    rex=curx+math.cos(math.radians(angle))*x + (-math.sin(math.radians(angle))*y)
    rey=curx+math.sin(math.radians(angle))*x + (math.cos(math.radians(angle))*y)
    t.goto(rex,rey)
    

