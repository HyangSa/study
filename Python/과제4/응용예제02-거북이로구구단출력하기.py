#_*_coding=cp949
#_*_coding: euc-kr
##
##응용예제02 - 거북이로 구구단 출력하기
import turtle # turtle 불러오기

## 전역 변수 선언 부분 ##
i, k, tX, tY = [0]*4 # 반복문, 거북이에 사용할 변수 선언
swidth, sheight=800,450 # 사이즈에 사용할 변수 선언

## 메인 코드 부분 ##
if __name__ == "__main__" :
    turtle.title('거북 구구단') # 그래픽 창 이름 지정
    turtle.shape('turtle') # 거북이 모양 지정
    turtle.setup(width = swidth + 50, height = sheight + 50) # 그래픽 창 크기 지정(850,500)
    turtle.screensize(swidth, sheight) # 켄버스의 크기 지정(800,450)
    turtle.penup() # 펜올리기
    tX, tY = -500, 250  # 좌표값 변수 초기화
    turtle.goto(tX, tY) # 거북이 지정 좌표로 이동(-500,250)

    for i in range(1, 10): # 1~9까지
        for k in range(2, 10): # 2~9까지
            turtle.goto(tX + 80 * k, tY - 40 * i) # 반복될때마다 좌표 이동(x좌표 증가,y좌표 감소)
            gugu = str(k) + ' x ' + str(i) + ' = ' + str(k * i) # 이중for문을 이용한 구구단(k x i = k*i)
            turtle.write(gugu, font=('Arial', 12, 'bold')) # 글자쓰기		  
    turtle.done()
