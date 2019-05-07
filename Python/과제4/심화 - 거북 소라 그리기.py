#_*_coding=cp949
#_*_coding: euc-kr
##
##응용예제02 - 거북이로 구구단 출력하기
import turtle # turtle 불러오기
import random as ran

## 전역 변수 선언 부분 ##
i, k, tX, tY = [0]*4 # 반복문, 거북이에 사용할 변수 선언
swidth, sheight=800,800 # 사이즈에 사용할 변수 선언

## 메인 코드 부분 ##
if __name__ == "__main__" :
    turtle.title('거북 구구단') # 그래픽 창 이름 지정
    turtle.shape('turtle') # 거북이 모양 지
    turtle.setup(width = swidth + 50, height = sheight + 50) # 그래픽 창 크기 지정(850,500)
    turtle.screensize(swidth, sheight) # 켄버스의 크기 지정(800,450)
    turtle.penup() # 펜올리기
    tX, tY = 0, 0  # 좌표값 변수 초기화
    turtle.goto(tX, tY) # 거북이 지정 좌표로 이동(-500,250)

    k=5
    turtle.pendown()
    turtle.pensize(5)
    turtle.speed(0)
    for i in range(0, 160): # 1~9까지
        r=ran.random()
        g=ran.random()
        b=ran.random()
        turtle.pencolor(r,g,b)
        turtle.forward(k)
        turtle.left(30)
        k=k+1
##        print(i)
        
    turtle.done()
