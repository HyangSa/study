#_*_coding=cp949
#_*_coding: euc-kr
##산술연산자
##[프로그램1]의 완성

## 변수 선언 부분 ##
money, c500, c100, c50, c10 = 0, 0, 0, 0, 0 #사용할 변수 선언

## 메인 코드 부분 ##
money = int(input("교환할 돈은 얼마?"))

c500 = money // 500     # (money / 500) 의 몫 대입
money %= 500    # (money = money % 500) money를 500으로 나눈 나머지 값 대입

c100 = money // 100     # (money / 100) 의 몫 대입
money %= 100    # (money = money % 100)

c50 = money // 50       # (money / 50) 의 몫 대입 
money %= 50     # (money = money % 50)

c10 = money // 10       # (money / 10) 의 몫 대입 
money %= 10     # (money = money % 10)

print("\n 500원 짜리 ==> %d개"%c500) # 변수 c500 출력 => (money / 500) 의 몫
print(" 100원 짜리 ==> %d개"%c100) # 변수 c100 출력 => (money / 100) 의 몫
print(" 50원 짜리  ==> %d개"%c50)  # 변수 c50 출력 => (money / 50) 의 몫
print(" 10원 짜리  ==> %d개"%c10)  # 변수 c10 출력 => (money / 10) 의 몫
print(" 바꾸지 못한 잔돈 ==> %d원 \n"%money) #남은 나머지값 출력
