#_*_coding=cp949
#_*_coding: euc-kr
## 2차원 리스트
## [프로그램 1]의 완성
import turtle
import random
##turtle.speed(0)
## 전역 변수 선언 부분 ##
myTurtle, tX, tY, tColor, tSize, tShape = [None]*6 # 거북이 속성 변수 선언
shapeList = [] # 모양 리스트 선언
playerTurtles = [] # 거북이 리스트 선언
swidth,sheight = 500, 500 # 사이즈 변수 선언
## 메인 코드 부분 ##
if __name__=="__main__":
    turtle.title("거북 리스트 활용") # 그래픽 창 이름 지정
    turtle.setup(width=swidth+50, height = sheight+50) # 그래픽 창 크기 지정
    turtle.screensize(swidth, sheight) # 켄버스의 크기 지정

    shapeList=turtle.getshapes() #거북이 모양 추출
    for i in range(0,100): # i:0~99까지 반복
        random.shuffle(shapeList) # 추출한 거북이 모양 순서 섞기
        myTurtle = turtle.Turtle(shapeList[0]) # 섞은 거북이 모양의 1번째 모양으로 거북이 모양 지정
        tX = random.randrange(-swidth/2,swidth/2) # X좌표 = -250~250 사이 (캔버스 좌측끝~우측끝 사이 난수)
        tY = random.randrange(-sheight/2,sheight/2) # Y좌표 = -250~250 사이 (맨 아래부터 맨 위 사이 난수)
        r=random.random();g=random.random();b=random.random() # r,g,b 색상 지정(0~1 난수)
        tSize=random.randrange(1,3) # 거북이 크기 지정(1~3)
        playerTurtles.append([myTurtle,tX,tY,tSize,r,g,b]) # 거북이 리스트에 거북이 속성에 관한 리스트 추가
        
    for tList in playerTurtles: # 리스트 하나씩 반복(처음부터 끝까지)
        myTurtle = tList[0] # 모양
        myTurtle.color((tList[4],tList[5],tList[6])) # 거북이 색
        myTurtle.pencolor((tList[4],tList[5],tList[6])) # 선 색
        myTurtle.turtlesize(tList[3]) # 거북이 크기
        myTurtle.goto(tList[1],tList[2]) # 이동 좌표
    turtle.done() # 창 유지.
#[[<turtle.Turtle object at 0x0000017CE9EE6A58>, -191, 199, 2, 0.5086602159715642, 0.06106201906133513, 0.4823624918923082]
