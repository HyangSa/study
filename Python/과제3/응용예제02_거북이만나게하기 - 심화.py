#_*_coding=cp949
#_*_coding: euc-kr
## 
## 응용예제 02 - 거북이가 서로 만나게 하기

import turtle # turtle 불러오기
import math   # math 불러오기
import random # random 불러오기

## 전역 변수 선언 부분 ##
t1, t2, t3 = [None] * 3 # 거북이에 사용할 변수 선언
t1X, t1Y, t2X, t2Y, t3X, t3Y = [0] * 6 # X,Y 좌표에 사용할 변수 선언
swidth, sheight = 300, 300 # 사이즈에 사용할 변수 선언

## 메인 코드 부분 ##
if __name__ == "__main__" :
    turtle.title('거북 만나기') # 그래픽 창 이름 지정
    turtle.setup(width = swidth + 50, height = sheight + 50) # 그래픽 창 크기 지정
    turtle.screensize(swidth, sheight) # 켄버스의 크기 지정
	
    t1 = turtle.Turtle('turtle'); t1.color('red');   t1.penup() # t1거북이 생성, 색상=빨강, 펜 올리기
    t2 = turtle.Turtle('turtle'); t2.color('green'); t2.penup() # t2거북이 생성, 색상=초록, 펜 올리기
    t3 = turtle.Turtle('turtle'); t3.color('blue'); t3.penup()  # t3거북이 생성, 색상=파랑, 펜 올리기
	
    t1.goto(-100, -100); t2.goto(0, 0); t3.goto(100, 100) # t1=-100,-100 t2=0,0 t3=100,100 각 좌표로 이동
    t1.speed(0); t2.speed(0); t3.speed(0) # 속도 지정

    while True : # 무한반복

        angle = random.randrange(0, 360) # 0~359사이의 난수를 각도로 사용
        dist = random.randrange(1, 50)   # 1~49 사이의 난수를 거리로 사용
        t1.left(angle); t1.forward(dist) # t1거북이 좌측으로 회전 및 직진
        angle = random.randrange(0, 360) # 0~359사이의 난수
        dist = random.randrange(1, 50)   # 1~49 사이의 난수
        t2.left(angle); t2.forward(dist) # t2거북이 좌측으로 회전 및 직진
        angle = random.randrange(0, 360) # 0~359사이의 난수
        dist = random.randrange(1, 50)   # 1~49 사이의 난수
        t3.left(angle); t3.forward(dist) # t3거북이 좌측으로 회전 및 직진

        t1X = t1.xcor(); t1Y = t1.ycor() # t1의 현재 x,y좌표 대입
        t2X = t2.xcor(); t2Y = t2.ycor() # t2의 현재 x,y좌표 대입
        t3X = t3.xcor(); t3Y = t3.ycor() # t3의 현재 x,y좌표 대입

        if (math.sqrt( ((t1X - t2X)*(t1X - t2X)) + ((t1Y - t2Y)*(t1Y - t2Y)) ) <= 20 or \
            math.sqrt( ((t1X - t3X)*(t1X - t3X)) + ((t1Y - t3Y)*(t1Y - t3Y)) ) <= 20 or \
            math.sqrt( ((t2X - t3X)*(t2X - t3X)) + ((t2Y - t3Y)*(t2Y - t3Y)) ) <= 20) :
            # (t1,t2), (t1,t3), (t2,t3) 거북이 거리 확인
            # 거북이의 거리가 20미만일때
            t1.turtlesize(3); t2.turtlesize(3); t3.turtlesize(3) # 거북이 사이즈 설정(3배)
            t1.stamp(); t2.stamp(); t3.stamp();
            t1.turtlesize(1); t2.turtlesize(1); t3.turtlesize(1)
        if (swidth/2 < t1X or t1X < -swidth/2) or (swidth/2 < t2X or t2X < -swidth/2) or (swidth/2 < t3X or t3X < -swidth/2) or \
           (sheight/2 < t1Y or t1Y < -sheight/2) or (sheight/2 < t1Y or t2Y < -sheight/2) or (sheight/2 < t1Y or t3Y < -sheight/2):
            t1.goto(-100, -100); t2.goto(0, 0); t3.goto(100, 100)
            
##            break # while문 탈출
        
turtle.done()
