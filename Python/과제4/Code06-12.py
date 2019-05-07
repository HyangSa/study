#_*_coding=cp949
#_*_coding: euc-kr
##break문과 continue문
##반복문을 탈출시키는 break문
hap = 0 # 변수 선언
a, b = 0, 0 # 변수 선언

while True : #무한반복
    a = int(input("더할 첫 번째 수를 입력하세요 : ")) # a 입력
    if a == 0 : # 입력받은 a가 일때
        break   # while문 탈출
    b = int(input("더할 두 번째 수를 입력하세요 : ")) # b 입력
    hap = a + b # 입력받은 a b 합
    print("%d + %d = %d" % (a, b, hap)) # 합 결과 출력 (a+b=hap)

print("0을 입력해 반복문을 탈출했습니다") #(while문 탈출 후) 내용 출력
