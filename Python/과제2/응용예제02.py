#_*_coding=cp949
#_*_coding: euc-kr
##연산자
##거북이로 2진수 숫자 표현하기
import turtle # turtle 불러오기

## 전역 변수 선언 부분 ##
num=0 #정수형 변수 선언
swidth, sheight = 1000, 300 # 사이즈에 사용할 변수 선언
curX, curY = 0, 0 # 좌표로 사용할 변수 선언

## 메인 코드 부분 ##
if __name__=='__main__':
    turtle.title('거북이로 2진수 표현하기') # 그래픽 창 이름 지정
    turtle.shape('turtle') # 터틀 모양 변경
    turtle.setup(width = swidth + 50, height = sheight + 50) # 그래픽 창 크기 지정(1050x350)
    turtle.screensize(swidth, sheight) # 켄버스의 크기 지정(1000x300)
    turtle.penup() # 펜 올리기
    turtle.left(90) # 반시계방향 90도 회전

    num = int(input("숫자를 입력하세요 : ")) # 정수 입력
    binary = bin(num) # binary에 입력받은 정수를 이진수로 변환하여 대입
    curX = swidth / 2 # 켄버스 크기의 반만큼 curX에 대입(curX=500)
    curY = 0 # y좌표로 사용할 값 대입
    for i in range(len(binary)-2): #이진수 길이 만큼 실행 (-2 = 0b 길이 소거)
        turtle.goto(curX,curY)  #거북이 좌표이동 초기값=(500,0)
        if num & 1 :            # 비트 논리곱 : (입력된 숫자 2진수) & 0001 --> (끝 값이 1이라면)
            turtle.color('red')     # 색상을 빨강색으로
            turtle.turtlesize(2)    # 거북이 크기를 2로 설정
        else :                  # (입력된 숫자 이진수 끝 값이 1이 아니라면)
            turtle.color('blue')    # 색상을 파랑색으로
            turtle.turtlesize(1)    # 거북이 크기를 1로 설정
        turtle.stamp()              # 커서모양 도장 찍기
        curX -= 50  # curX = curX - 50 (거북이 x좌표 -50)
        num >>= 1   # num = num >> 1 (시프트연산 한번)
 
turtle.done()
            
