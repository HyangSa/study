#_*_coding=cp949
#_*_coding: euc-kr
## (05)모듈
## [프로그램2]의 완성
import random # random 불러오기
from tkinter.simpledialog import * # tkinter.simpledialog 불러오기

def getString(): # 함수 이름 정의
    retStr = '' # 변수 선언
    retStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력') #문자열 입력
    return retStr # 입력받은 문자열로 결과값 반환

def getRGB(): # 함수 이름 정의
    r,g,b = 0,0,0 # 변수 선언
    r = random.random() # 0~1사이 난수 대입
    g = random.random() # 0~1사이 난수 대입
    b = random.random() # 0~1사이 난수 대입
    return (r,g,b)  # r,g,b 변수값 반환

def getXYAS(sw,sh): # 함수 이름, 인수(2) 반환
    x,y,angle,size = 0,0,0,0 # 변수 선언
    x = random.randrange(-sw / 2, sw / 2) # (-인수1/2)~(인수1/2) 사이 난수 대입
    y = random.randrange(-sh / 2, sh / 2) # (-인수2/2)~(인수2/2) 사이 난수 대입
    angle = random.randrange(0,360) # 0~360 사이 난수 대입
    size = random.randrange(10,50) #10~50 사이의 난수 대입
    return [x,y,angle,size] # x,y,angle,size 변수값 반환
