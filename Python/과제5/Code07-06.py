#_*_coding=cp949
#_*_coding: euc-kr
## 2차원 리스트
## 2차원 리스트의 개념
list1=[] # 리스트1 선언
list2=[] # 리스트2 선언
value=1 # 값 초기화(1)
for i in range(0,3): # i:0~2 까지 반복
    for k in range(0,4): # k:0~3까지 반복
        list1.append(value) # 리스트1에 값 추가
        value+=1 # 값=1씩 증가
    list2.append(list1) # 리스트2에 리스트1 추가(i:0~2까지 반복에 포함)
    list1=[] # 리스트1 초기화
#3행 4열짜리 리스트 작성 완료
for i in range(0,3): # 0~2까지 반복
    for k in range(0,4): # 0~3까지 반복
        print("%3d" %list2[i][k], end="") # list2[0][0]~list[2][3]까지 출력
    print("") # k가 0~3까지 한 후 줄바꿈(i의 반복문에 포함)
