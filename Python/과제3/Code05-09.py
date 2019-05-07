#_*_coding=cp949
#_*_coding: euc-kr
##중첩 if문
##[프로그램 1]의 완성

import turtle # turtle 불러오기
## 전역 변수 선언 부분 ##
swidth, sheight = 500, 500 # 사이즈에 사용할 변수 선언
## 메인 코드 부분 ##
turtle.title('무지개색 원그리기') # 그래픽 창 이름 지정
turtle.shape('turtle') # 터틀 모양 변경
turtle.setup(width = swidth + 50, height = sheight + 50) # 그래픽 창 크기 지정(550x550)
turtle.screensize(swidth, sheight)# 켄버스의 크기 지정(500x500)
turtle.penup() # 펜 올리기
turtle.goto(0, -sheight / 2) # 지정좌표로 이동(0,-250)
turtle.pendown() # 펜 내리기
turtle.speed(0) # 속도 조정

for radius in range(1, 250) : # 1~249까지 반복 실행(radius 1씩 증가)
    if radius % 6 == 0 : # radius/6 나머지가 0일때
        turtle.pencolor('red') # 펜색상 변경(빨강)
    elif radius % 5 == 0 : # radius/5 나머지가 0일때
        turtle.pencolor('orange') # 펜색상 변경(주황)
    elif radius % 4 == 0 : # radius/4 나머지가 0일때
        turtle.pencolor('yellow') # 펜색상 변경(노랑)
    elif radius % 3 == 0 : # radius/3 나머지가 0일때
        turtle.pencolor('green')  # 펜색상 변경(초록)
    elif radius % 2 == 0 : # radius/2 나머지가 0일때
        turtle.pencolor('blue')   # 펜색상 변경(파랑)  
    elif radius % 1 == 0 : # radius/1 나머지가 0일때
        turtle.pencolor('navyblue') # 펜색상 변경(남색)  
    else :  # 그 외일때 
        turtle.pencolor('purple') # 펜색상 변경(보라)  
    turtle.circle(radius) # 원그리기(radius을 반지름으로 한 원)
turtle.done()
