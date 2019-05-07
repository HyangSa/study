#58쪽
#계산기 터틀로.

import turtle as t
import random

r,g,b=0.0,0.0,0.0

def LClick(x,y):
    global r,g,b
    tSize=random.randrange(1,10)
    tDeg=random.randrange(1,360)
    t.shapesize(tSize)
    r=random.random()
    g=random.random()
    b=random.random()
    t.penup()
    t.color(r,g,b)
    t.setheading(tDeg)
    t.goto(x,y)
    t.stamp()

def tstem():
    t.title('거북이 그림그리기')
    t.shape('turtle')
    t.speed(0)
    t.onscreenclick(LClick,1)

