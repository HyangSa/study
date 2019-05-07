#_*_coding=cp949
#_*_coding: euc-kr
##산술연산자
##[프로그램1]의 완성

## 변수 선언 부분 ##
money, c50000, c10000, c5000, c1000 = 0, 0, 0, 0, 0 #사용할 변수 선언

## 메인 코드 부분 ##
money = int(input("교환할 돈은 얼마?"))

c50000 = money // 50000     # (money / 500) 의 몫 대입
money %= 50000    # (money = money % 500) money를 500으로 나눈 나머지 값 대입

c10000 = money // 10000     # (money / 100) 의 몫 대입
money %= 10000    # (money = money % 100)

c5000 = money // 5000       # (money / 50) 의 몫 대입 
money %= 5000     # (money = money % 50)

c1000 = money // 1000       # (money / 10) 의 몫 대입 
money %= 1000     # (money = money % 10)

print("\n 오만원 짜리 ==> %d개"%c50000) # 변수 c500 출력 => (money / 500) 의 몫
print(" 만원 짜리   ==> %d개"%c10000) # 변수 c100 출력 => (money / 100) 의 몫
print(" 오천원 짜리 ==> %d개"%c5000)  # 변수 c50 출력 => (money / 50) 의 몫
print(" 천원 짜리   ==> %d개"%c1000)  # 변수 c10 출력 => (money / 10) 의 몫
print(" 바꾸지 못한 잔돈 ==> %d원 \n"%money) #남은 나머지값 출력
