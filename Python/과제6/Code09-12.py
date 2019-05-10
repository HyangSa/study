#_*_coding=cp949
#_*_coding: euc-kr
## 함수의 반환값과 매개변수
## 함수의 매개변수 전달
## 함수 선언 부분 ##
def para_func(*para):# 함수 이름, 인수 정의 (*를 사용하면 튜플 **를 사용하면 사전)
    result = 0       # 결과변수 선언(초기화)
    for num in para :# 입력받은 인수만큼 반복 (순서대로 num에 대입)
        result = result + num # 결과=결과+num (num 중첩)
    return result # 결과값 반환

## 전역 변수 선언 부분 ##
hap = 0 # 전역변수 선언

## 메인 코드 부분 ##
hap = para_func(10, 20) # 함수 반환값 대입(10+20)
print("매개변수가 2개인 함수를 호출한 결과 ==> %d" %hap) # 결과 출력
hap = para_func(10, 20, 30) # 함수 반환값 대입(10+20+30)
print("매개변수가 3개인 함수를 호출한 결과 ==> %d" %hap) # 결과 출력
