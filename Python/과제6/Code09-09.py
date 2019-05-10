#_*_coding=cp949
#_*_coding: euc-kr
## 함수의 반환값과 매개변수
## 함수의 반환값
## 함수 선언 부분 ##
def multi(v1,v2): # 함수 이름, 인수 정의
    retList=[]      # 반환할 리스트
    res1 = v1 + v2  # 결과1=인수1+인수2
    res2 = v1 - v2  # 결과2=인수1-인수2
    retList.append(res1) # 반환할 리스트에 결과1 추가
    retList.append(res2) # 반환할 리스트에 결과2 추가
    return retList # 결과리스트 반환
	
## 전역 변수 선언 부분 ##
myList=[] # 전역변수 선언
hap,sub = 0,0 # 사용할 전역변수 선언

## 메인 코드 부분 ##
myList = multi(100, 200) # 변수에 multi함수 반환값 대입
hap = myList[0] # hap에 대입된 리스트 1번째 값 대입
sub = myList[1] # sub에 대입된 리스트 2번째 값 대입
print("multi()에서 돌려준 값 ==> %d, %d" %(hap,sub)) # 결과 출력
