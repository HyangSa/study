#_*_coding=cp949
#_*_coding: euc-kr
## (05)모듈
## [프로그램2]의 완성
from myTurtle import * # myTurtle.py 불러오기
import turtle # turtle 불러오기

## 전역 변수 선언 부분 ##
inStr=''# 글자 변수 선언
swidth,sheight = 300,300 # 사이즈에 사용할 변수 선언
tX,tY,tAngle,txtSize = [0]*4 # 좌표값,각도,글자크기 변수 초기화

## 메인 코드 부분 ##
turtle.title('거북이 글자쓰기(모듈버전)') # 그래픽 창 이름 지정
turtle.shape('turtle') # 거북이 모양 지정
turtle.setup(width = swidth + 50, height = sheight + 50) # 그래픽 창 크기 지정
turtle.screensize(swidth, sheight) # 켄버스의 크기 지정
turtle.penup() # 펜올리기
turtle.speed(5) # 거북이 속도 지정(5)

inStr=getString() # myTurtle의 getString 함수 실행(반환값 대입)

for ch in inStr : # inStr값 순서대로 ch에 대입하여 실행
    
    tX,tY,tAngle,txtSize = getXYAS(swidth, sheight)
    # myTurtle의 getXYAS 함수 실행 (반환값 대입: tX,tY,tAngle,txtSize=[x,y,angle,size])
    r,g,b = getRGB()  # myTurtle의 getRGB 함수 실행 r,g,b에 반환값 대입

    turtle.goto(tX,tY) # 거북이 좌표 이동
    turtle.left(tAngle) # 거북이 각도 회전(좌측)

    turtle.pencolor((r,g,b)) # 대입된 r,g,b 값으로 거북이 색상 변경
    turtle.write(ch, font=('맑은고딕', txtSize, 'bold')) # inStr에서 대입받은 ch 글자 쓰기
				
turtle.done() # 창 유지

