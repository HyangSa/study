#_*_coding=cp949
#_*_coding: euc-kr
##변수와데이터형
##응용예제01 데이터형 크기 확인하기
import sys

## 변수 선언 부분 ##
intVar,floatVar,boolVar,strVar,listVar,tupleVar,dicVar,setVar=[None]*8 #전역변수 8개 선언


## 메인 코드 부분 ##
if __name__=='__main__':
    intVar=0      # 정수형 대입
    floatVar=0.0    # 실수형 데이터 대입
    boolVar=True    # 논리형 데이터 대입
    strVar=""       # 문자열 데이터 대입
    listVar=[]      # 리스트형 데이터 대입
    tupleVar=()     # 튜플형 데이터 대입
    dicVar={}       # 딕셔너리형 데이터 대입
    setVar=set()    # 집합형 데이터 대입

    print('int형 기본 크기 -->', sys.getsizeof(intVar))       # 
    print('float형 기본 크기 -->', sys.getsizeof(floatVar))   #
    print('bool형 기본 크기 -->', sys.getsizeof(boolVar))     # sys.getsizeof() => 크기를 byte단위로 return
    print('str형 기본 크기 -->', sys.getsizeof(strVar))       # 각 데이터형의 기본크기를 byte단위로 출력
    print('list형 기본 크기 -->', sys.getsizeof(listVar))     #
    print('tuple형 기본 크기 -->', sys.getsizeof(tupleVar))   #
    print('dictionary형 기본 크기 -->', sys.getsizeof(dicVar))#
    print('set형 기본 크기 -->', sys.getsizeof(setVar))       #
