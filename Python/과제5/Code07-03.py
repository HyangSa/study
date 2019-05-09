#_*_coding=cp949
#_*_coding: euc-kr
## 리스트의 기본
## 리스트의 일반적인 사용
aa=[] # 빈 리스트 변수 선
for i in range(0,4): # 0~3까지 반복
    aa.append(0) # 리스트 추가 값=0
hap=0 # 결과로 사용할 변수 선언(초기화)

for i in range(0,4): # 0~3까지 반복
    aa[i]=int(input(str(i+1)+"번째 숫자 : ")) # 1~4번째 숫자 입력(정수)

hap=aa[0]+aa[1]+aa[2]+aa[3] #입력받은 값 합계

print("합계 ==> %d" %hap) # 결과 출력
