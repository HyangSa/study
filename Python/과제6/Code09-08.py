#_*_coding=cp949
#_*_coding: euc-kr
## 함수의 반환값과 매개변수
## 함수의 반환값
## 함수 선언 부분 ##
def func1(): # 함수 이름 정의
    result = 100 # 결과값=100 대입
    return result # 결과값 반환

def func2(): # 함수 이름 정의
    print("반환값이 없는 함수 실행") # 내용 출력
	
## 전역 변수 선언 부분 ##
hap = 0 # 전역변수 선언

## 메인 코드 부분 ##
hap = func1() # 함수1 실행(hap에 반환값 대입)
print("func1()에서 돌려준 값 ==> %d" %hap) # 결과 출력
func2() # 함수2 실행(hap에 대입해도 아무것도 대입되지 않는다)
