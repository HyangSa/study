#_*_coding=cp949
#_*_coding: euc-kr
## 중첩 for문
## [프로그램 1]의 완성

## 전역 변수 선언 부분 ##
i, k, guguLine = 0, 0, "" #변수선언

## 메인 코드 부분 ##
for i in range(2, 10) : # 2~9까지 반복
    guguLine = guguLine + (" #  %d단  #" %i) #guguLine = # 2단...9단 #

print(guguLine) # 2단...9단 # 출력

for i in range(1, 10) : # 1~9까지 반복
    guguLine = "" # guguLine 초기화
    for k in range(2, 10) : # 2~9까지 반복
        guguLine = guguLine + str("%2d X%2d= %2d" %(k, i, k*i))
        # guguLine = guguLine + k(2~9까지) X i(1) = k*i
        # guguLine = guguLine + k(2~9까지) X i(2) = k*i
        # guguLine = guguLine + k(2~9까지) X i(3) = k*i
        #              ...
        # guguLine = guguLine + k(2~9까지) X i(9) = k*i
    print(guguLine) # guguLine 출력
