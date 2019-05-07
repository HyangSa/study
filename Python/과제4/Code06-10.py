#_*_coding=cp949
#_*_coding: euc-kr
## while문
## 무한 루프를 하는 while문
hap = 0 # 변수 선언
a, b = 0, 0 # 입력받을 변수 선언(초기화)

while True : # 무한 반복
    a = int(input("더할 첫 번째 수를 입력하세요 : ")) # a 입력
    b = int(input("더할 두 번째 수를 입력하세요 : ")) # b 입력
    hap = a + b # 입력받은 두수 합
    print("%d + %d = %d" % (a, b, hap)) # 결과 출력 (a+b=hap)
