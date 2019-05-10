#_*_coding=cp949
#_*_coding: euc-kr
## 함수의 반환값과 매개변수
## [프로그램1]의 완성
import random # random불러오기

## 함수 선언 부분 ##
def getNumber(): # 함수 이름 정의
    return random.randrange(1,46) # 반환값=1~46사이의 난수

## 전역 변수 선언 부분 ##
lotto=[] # 전연변수 리스트형 선언
num=0 # 전역변수 선언

## 메인 코드 부분 ##
print("** 로또 추첨을 시작합니다. ** \n") # 내용 출력

while True : # 무한 반복
    num = getNumber() #getNumber의 반환값(1~46사이의 난수) 대입

    if lotto.count(num)==0 : #num대입된 값이 lotto리스트에 개수가 0이라면
        lotto.append(num) # lotto리스트에 추가

    if len(lotto)>=6 : # lotto리스트 길이가 6과 같거나 크면
        break # 반복 중지(while문 탈출)

print("추첨된 로또 번호 ==> ", end='') # 내용 출력(줄바꿈X)
lotto.sort()# lotto리스트 순서 정렬
for i in range(0, 6): # 0~5까지 반복
    print("%d " %lotto[i], end='') # lotto리스트 i번째 값 출력(줄바꿈X)
##[print(n,end=' ') for n in lotto]
