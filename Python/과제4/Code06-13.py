#_*_coding=cp949
#_*_coding: euc-kr
##break문과 continue문
##반복문을 탈출시키는 break문
hap, i = 0,0 # 변수 선언

for i in range(1,101): # i = 1~100까지 반복
    hap += i # i 중첩

    if hap >= 1000 : # i중첩값(hap)이 1000보다 같거나 클 경우
        break # while문 탈출 

print("1~100의 합계를 최초로 1000이 넘게 하는 숫자 : %d" % i)
# 중첩값이 1000을 넘었을때(while문 탈출 때) i의 값 출력
