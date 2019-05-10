#_*_coding=cp949
#_*_coding: euc-kr
## 함수 기본
## 함수의 형식과 활용
## 함수 선언 부분 ##
def calc(v1,v2,op): # 함수 이름, 인수 정의
    result = 0 # 결과값 선언(초기화)
    if op == '+' :  # op 인수가 '+'일때
        result = v1 + v2 # 결과=인수1+인수2
    elif op == '-' :# op 인수가 '-'일때
        result = v1 - v2 # 결과=인수1-인수2
    elif op == '*' :# op 인수가 '*'일때
        result = v1 * v2 # 결과=인수1*인수2
    elif op == '/' :# op 인수가 '/'일때
        result = v1 / v2 # 결과=인수1/인수2
	
    return result # 결과값 반환

## 전역 변수 선언 부분 ##
res = 0 # 변수 선언
var1, var2, oper = 0, 0, "" # 변수 선언(초기화)

## 메인 코드 부분 ##
oper = input("계산을 입력하세요(+, -, *, /) : ") # op인수 입력
var1 = int(input("첫 번째 수를 입력하세요 : "))  # v1인수 입력
var2 = int(input("두 번째 수를 입력하세요 : "))  # v2인수 입력

res = calc(var1,var2,oper) # 입력받은 인수로 함수 실행

print("## 계산기 : %d %s %d = %d" %(var1, oper, var2, res)) # 입력값과 결과 출력
