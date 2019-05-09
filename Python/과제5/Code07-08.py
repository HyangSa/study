#_*_coding=cp949
#_*_coding: euc-kr
## 딕셔너리
## 딕셔너리의 사용
singer = {} # 딕셔너리 변수선언

singer['이름']='트와이스' # 키:이름, 값:트와이스
singer['구성원 수']=9 # 키:구성원수, 값:9
singer['데뷔']='서바이벌 식스틴' # 키:데뷔, 값:서바이벌 식스틴
singer['대표곡']='SIGNAL' # 키:대표곡, 값:SIGNAL

for k in singer.keys(): # 키 하나씩 처음부터 끝까지
    print('%s --> %s' %(k,singer[k])) # 결과 출력(키, 값)
