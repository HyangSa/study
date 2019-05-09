#_*_coding=cp949
#_*_coding: euc-kr
## 응용예제01
## 16진수 정렬
import random # 랜덤 불러오기

## 변수 선언 부분 ##
data=[] # data 리스트 선언
i,k=0,0 # 변수 2개 선언(초기화)
## 메인 코드 부분 ##
if __name__=="__main__":
    for i in range(0,10): # 0~9까지 반복(10번)
        tmp=hex(random.randrange(0,100000)) # 0~100000사이의 난수 16진수 tmp에 대입
        data.append(tmp) # data리스트에 16진수 값추가

    print("정렬 전 데이터: ", end='') # 내용 출력
    [print(num,end=' ') for num in data] #(컴프리헨션) 리스트 값 출력

    for i in range(0, len(data)-1): # 0~data길이-1까지 반복(0~9)
        for k in range(i+1, len(data)): # i+1~9까지 반복(i가 증가함에따라 횟수-1)
            if int(data[i],16) > int(data[k], 16):
                #데이터 리스트의 i번째 정수값 > 데이터리스트의 k번째 정수값이 참이면
                tmp=data[i] # 임시 변수에 리스트의 i번째 값 대입
                data[i]=data[k] # 리스트 i번째 위치에 리스트의 k번째 값 대입
                data[k]=tmp # 리스트 k번째 위치에 위에 대입해 놨던 i번째 값 대입

    print("\n정렬 후 데이터: ", end='') # 내용 출력
    [print(num,end=' ') for num in data] #(컴프리헨션) 리스트 값 출력
