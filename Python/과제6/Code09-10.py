#_*_coding=cp949
#_*_coding: euc-kr
## 함수의 반환값과 매개변수
## 함수의 매개변수 전달
## 함수 선언 부분 ##
def para2_func(v1,v2): # 함수 이름, 인수(2) 정의
    result = 0       # 결과변수 선언(초기화)
    result = v1 + v2 # 결과=인수1+인수2
    return result    # 결과값 반환

def para3_func(v1,v2,v3): # 함수 이름, 인수(3) 정의
    result = 0            # 결과변수 선언(초기화)
    result = v1 + v2 + v3 # 결과=인수1=인수2=인수3
    return result         # 결과값 반환

## 전역 변수 선언 부분 ##
hap = 0 # 전역변수 선언

## 메인 코드 부분 ##
hap = para2_func(10, 20) # para2함수 반환값 대입
print("매개변수가 2개인 함수를 호출한 결과 ==> %d" %hap) # 결과 출력
hap = para3_func(10, 20, 30) # para3함수 반환값 대입
print("매개변수가 3개인 함수를 호출한 결과 ==> %d" %hap) # 결과 출력
