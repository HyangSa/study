#_*_coding=cp949
#_*_coding: euc-kr
## 논리 연산자
## [프로그램 2]의 완성
import turtle
import random
## 전역 변수 선언 부분 ##
swidth, sheight, pSize, exitCount = 300, 300, 3, 0 #변수 4개 선언
r, g, b, angle, dist, curX, curY = [0]*7 #변수 7개 선언

## 메인 코드 부분 ##
turtle.title('거북이가 맘대로 다니기') #그래픽 창 이름 지정
turtle.shape('turtle') # 터틀 모양 변경
turtle.pensize(pSize)   #선 두께 설정(3)
turtle.setup(width=swidth+30,height=sheight+30) #그래픽 창 크기 지정(330x330)픽
turtle.screensize(swidth,sheight) #켄버스의 크기 지정(300x300)

while True :
    r = random.random() #변수 r에 0~1의 난수 대입
    g = random.random() #변수 g에 0~1의 난수 대입
    b = random.random() #변수 b에 0~1의 난수 대입
    turtle.pencolor((r,g,b)) # 변수 r,g,b로 팬 색상 지정

    angle = random.randrange(0,360) # angle에 0~359 사이의 난수 대입
    dist = random.randrange(1,100) # dist에 1~99 사이의 난수 대입
    turtle.left(angle)  # 좌측으로 angle만큼 회전
    turtle.forward(dist) # dist만큼 직진
    curX = turtle.xcor() # curX = 현재 거북이 x좌표
    curY = turtle.ycor() # curY = 현재 거북이 y좌표

    if (-swidth/2<=curX and curX<=swidth/2) and \
       (-sheight/2<=curY and curY<=sheight/2) :
        pass # 거북이의 x,y좌표가 켄버스 크기 안에 있을 경우 if문 통과
    else :   # 조건식에 참이 아닐 경우
        turtle.penup()  # 펜 올리기
        turtle.goto(0,0)# 0,0 좌표로 거북이 이동
        turtle.pendown()# 펜 내리기

        exitCount += 1 # exitCount 1 증가
        if exitCount >= 5 : # exitCount 가 5이상일 경우 
            break # while문 탈출
turtle.done() #Tkinter의 mainloop 함수를 호출
