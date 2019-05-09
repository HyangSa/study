#_*_coding=cp949
#_*_coding: euc-kr
## 리스트의 기본
## 리스트의 생성과 초기화
aa=[] # 빈 리스트 변수 선언
bb=[] # 빈 리스트 변수 선언
value=0 # 변수 값 선언

for i in range(0,100): # 0~99 까지 반복
    aa.append(value) #리스트에 값 추가
    value+=2 # 값 : (0부터 2씩 증가)

for i in range(0,100): # 0~99 까지 반복
    bb.append(aa[99-i]) # aa의 리스트 99~0 순으로 bb리스트에 값 추가

print("bb[0]에는 %d이, bb[99]에는 %d이 입력됩니다." %(bb[0],bb[99]))
# bb 리스트의 1번째 값과 마지막 값 출력
