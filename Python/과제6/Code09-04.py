#_*_coding=cp949
#_*_coding: euc-kr
## 함수 기본
## 함수의 형식과 활용
## 함수 선언 부분 ##
def plus(v1,v2): # 함수 이름, 인수 정의
    result = 0 # 결과값 선언(초기화)
    result = v1+v2 # 결과=인수1+인수2
    return result # 결과값 반환

## 전역 변수 선언 부분 ##
hap = 0 # 전역변수 선언

## 메인 코드 부분 ##
hap = plus(100,200) #함수 사용 대입(hap=100+200)
print("100과 200의 plus() 함수 결과는 %d" %hap) # 결과값 출력
