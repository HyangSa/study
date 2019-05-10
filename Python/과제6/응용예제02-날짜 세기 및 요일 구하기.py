#_*_coding=cp949
#_*_coding: euc-kr
##날짜 세기 및 요일 구하기
from time import * # time 불러오기
from datetime import * # datetime 불러오기
## 함수 선언 부분 ##
def countDays(date1,date2): # 날짜 수 세기(함수 이름, 인수 정의)
    retDays = 0 # 변수 선언
    year, month, day = date1.split('/') # '/'기준으로 값을 나누어 리스트로 반환
    sDay = date(int(year), int(month), int(day))
    # 위에서 얻은 값을 정수로 입력하여 date객체 대입
    year, month, day = date2.split('/') # '/'기준으로 값을 나누어 리스트로 반환
    eDay = date(int(year), int(month), int(day))
    # 위에서 얻은 값을 정수로 입력하여 date객체 대입
    diffDays = eDay - sDay # 두 날짜의 차 계산
    retDays = diffDays.days # 날짜만 추출
    return retDays # 결과값 반환

def getDay(t):  # 요일 구하기
    weeks = ['월', '화', '수', '목', '금', '토', '일'] # 0~6 월~일 순으로 리스트 생성
    return weeks[t.tm_wday] # tm_wday는 요일(월요일~일요일, 0~6)으로 반환

## 전역 변수 선언 부분 ##
startDate, curDate, tm = '', '', None

## 메인 코드 부분 ##
if __name__ == "__main__" :

    startDate = input('시작 날짜(연/월/일) --> ') #시작 날짜 입력
    tm = localtime() # 시스템기준의 현재시간을 struct_time로 tm에 대입
    curDate = str(tm.tm_year)+'/'+str(tm.tm_mon)+'/'+str(tm.tm_mday)
    # tm변수에서 받아온 struct_time타입의 객체에서 년도/월/일 형식으로 속성을 읽어와 대입

    print(startDate, '부터 오늘(',curDate,')까지는 ', countDays(startDate, curDate), '일이 지났습니다')
    # startDate, curDate, countDays함수를 사용하여 두 날짜의 차(일수) 출력
    print('그리고 오늘은 ',getDay(tm),'요일입니다')
    # 현재 시간을 인수로 사용하여 getDay 함수 호출 - 요일 출력
