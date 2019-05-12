import pdb
################       TIC     ###################
import time
t=time.time()
##elapsed = time.time() - t

## 1.
table1=[[0,0,0,0,0,0,0,0,0,0] for i in range(10)] #10X10 2차 리스트 생성
table2=[[0,0,0,0,0,0,0,0,0,0] for i in range(10)] #10X10 2차 리스트 생성

##print("-----  1. 10X10 2차원 리스트 -----")
##print("-----  table1")
##[print(table1[i]) for i in range(10)] # 1행씩 리스트 출력
##print("-----  table2")
##[print(table2[j]) for j in range(10)] # 1행씩 리스트출력
###################################################
###################################################

## 2.
import random # random 불러오기
tmp1=[i for i in range(1,101)] # 1~100 리스트 생성
tmp2=[j for j in range(101,201)] # 101~200 리스트 생성

for i in range (0,10): # i=>0~9
    for j in range (0,10): # j=>0~9
        if len(tmp1)!=1: # tmp1 리스트 길이가 1이 아니면
            table1[i][j]=tmp1.pop(random.randrange(0,len(tmp1)-1))
            # (0~tmp1리스트길이-1 사이의 난수) 위치 값 빼서 table1에 대입
        else: # tmp1 리스트 길이가 1이면
            table1[i][j]=tmp1[0] # tmp1 리스트 0 위치의 값 table1에 대입
        if len(tmp2)!=1: # tmp2 리스트 길이가 1이 아니면
            table2[i][j]=tmp2.pop(random.randrange(0,len(tmp2)-1))
            # (0~tmp2리스트길이-1 사이의 난수) 위치 값 빼서 table2에 대입
        else: # tmp2 리스트 길이가 1이면
            table2[i][j]=tmp2[0] # tmp2 리스트 0 위치의 값 table2에 대입

##print("\n------ 2. 랜덤 ------") # 내용 출력
##for i in range (0,20): # i=>0~19
##    if i==0: print("----- table1") # i=0 일때 출력(table1 앞)
##    if i==10: print("----- table2") # i=10 일때 출력(table2 앞)
##    for j in range (0,10): # j=>0~9
##        if i<10: # i<10 일때
##            print(" %3d" %table1[i][j],end='') # table1 값 1개씩 출력
##        else: # i<10 이 아닐때
##            print(" %3d" %table2[i-10][j],end='') # table2 값 1개씩 출력
##        if j==9: print() # 값 10번 출력 후 줄바꿈
####[print(table1[i]) for i in range(10)]
####[print(table2[j]) for j in range(10)]
        
###################################################
###################################################


## 4.
def mergeSort(x): # 함수 이름, 인수 정의
    if len(x) > 1: # x(받아온 리스트) 길이가 1보다 클때
        lx, rx = x[:len(x)//2], x[len(x)//2:] # x길이//2를 통해 왼쪽x 오른쪽x로 반 나눔
##        print(lx,rx)
        mergeSort(lx) # 반으로 나눈 x(lx)로 다시 mergeSort(함수 실행) 재귀
        mergeSort(rx) # 반으로 나눈 x(rx)로 다시 mergeSort(함수 실행) 재귀
        
        leftc,rightc,c=0,0,0
        # leftc=왼쪽 리스트 위치 카운트 / rightc=오른쪽 리스트 위치 카운트 / c=나누기전의 리스트 위치 카운트
        while len(lx)>leftc and len(rx)>rightc : # 양쪽 리스트 위치 카운트가 리스트 안에 있다면 (반복)
            if lx[leftc] < rx[rightc]: # lx의 leftc위치의 값이 rx의 rightc위치의 값보다 작을때
                x[c]=lx[leftc] # 나누기 전의 리스트의 c위치에 lx의 leftc위치의 값 대입(작은 값 대입)
                leftc+=1 # 왼쪽 리스트 위치 카운트 +1
            else : # 오른쪽 값이 더 작다면
                x[c]=rx[rightc] # 나누기 전의 리스트의 c위치에 rx의 rightc위치의 값 대입(작은 값 대입)
                rightc+=1 # 오른쪽 리스트 위치 카운트 +1
            c+=1 # 나누기 전의 리스트 위치 카운트 +1
##            pdb.set_trace()
        if leftc ==len(lx): # 왼쪽 리스트 위치가 끝까지 가면
            x[c:]=rx[rightc:] # 남은 오른쪽 값 들을 나누기 전 리스트(대입이 되지 않은곳)에 전부 대입
        if rightc ==len(rx): # 오른쪽 리스트 위치가 끝까지 가면
            x[c:]=lx[leftc:] # 남은 왼쪽 값 들을 나누기 전 리스트(대입이 되지 않은곳)에 전부 대입
        return x # 비교 후 다시 대입 된 리스트를 반환

list1=mergeSort([table1[i][j] for i in range(10) for j in range(10)])
#list1 = mergeSort(table1을 1차 리스트로 만든 리스트)
list2=mergeSort([table2[i][j] for i in range(10) for j in range(10)])
#list2 = mergeSort(table2을 1차 리스트로 만든 리스트)

k=0; # 1차 리스트 카운트 값 변수
t1=[[0,0,0,0,0,0,0,0,0,0] for i in range(10)] # 10X10리스트 생성
t2=[[0,0,0,0,0,0,0,0,0,0] for i in range(10)] # 10X10리스트 생성
for i in range(10): # i=>0~9
    for j in range(10): # j=>0~9
        t1[i][j]=list1[k] # t1에 list1 값 대입
        t2[i][j]=list2[k] # t2에 list2 값 대입
        k+=1 # k=>0~99
##print("\n----- 4.table1,2 합병정렬 -----")
##for i in range (0,20): #i=>0~19
##    if i==0: print("----- table1")  # i=0 일때 출력(table1 앞)
##    if i==10: print("----- table2") # i=10 일때 출력(table2 앞)
##    for j in range (0,10):# j=>0~9
##        if i<10: # i<10 일때
##            print(" %3d" %t1[i][j],end='')    # table1 값 1개씩 출력
##        else:    # i<10이 아닐때
##            print(" %3d" %t2[i-10][j],end='') # table2 값 1개씩 출력
##        if j==9: print() # 값 10번 출력 후 줄바꿈
####[print(table1[i]) for i in range(10)]
####[print(table2[j]) for j in range(10)]


## quickSort(), bubbleSort(), mergeSort(), insertionSort, selectionSort()
# 합병정렬 이후 사용  11%4=3 ==> 삽입 정렬


##print("\n----- 4.table3 삽입 정렬 -----")
table3=table1+table2 # table3 = table1,2의 합
##print("----- table3 정렬 전")
##[print(table3[j]) for j in range(20)] # 1행씩 리스트 출력

def insertionSort(x): # 함수 이름, 인수 정의
    for no in range(1,len(x)): # no=>1~받아온 리스트(x)길이-1
        num = x[no] # 리스트 no위치의 값 num에 대입
        backno = no-1 # backno = 리스트 위치-1
        while backno>=0 and x[backno] > num: # 값이 작으면 왼쪽으로 이동(반복)
            # 리스트의 범위안이고 no위치에서 대입받은 값이 리스트의 전 위치의 값보다 작다면
            x[backno+1]=x[backno] # 전(왼쪽)의 값을 앞 위치에 대입 (값 오른쪽으로 이동)
            backno-=1 # 비교할 리스트 위치 -1 
        x[backno+1]=num
        # 작은값 왼쪽이동이 끝난 후(값이 왼쪽보다 크면) num값을 오른쪽으로 이동하지 않고 제자리에 대입
    return x # 정렬된 리스트 반환

list3=insertionSort([table3[i][j] for i in range(20) for j in range(10)])
#list3 = insertionSort(table3을 1차 리스트로 만든 리스트)

k=0 # 1차 리스트 카운트 값 변수
for i in range(20): # i=>0~19
    for j in range(10): # j=>0~9
        table3[i][j]=list3[k] # table3에 list3 값 대입
        k+=1 # k=>0~199

print("----- table3 삽입 정렬 후")
for i in range (0,20): # i=>0~19
    for j in range (0,10): # j=>0~9
        print(" %3d" %table3[i][j],end='') # table3 값 1개씩 출력
        if j==9: print() # 값 10번 출력 후 줄바꿈
####[print(table3[i]) for i in range(20)]
