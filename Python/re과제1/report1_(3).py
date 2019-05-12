import pdb
################       TIC     ###################
import time
t=time.time()
##elapsed = time.time() - t

## 1.
table1=[]
table2=[]

table1=[[0,0,0,0,0,0,0,0,0,0] for i in range(10)]
table2=[[0,0,0,0,0,0,0,0,0,0] for i in range(10)]

##print("-----  1. 10X10 2차원 리스트 -----")
##print("-----  table1")
##[print(table1[i]) for i in range(10)]
##print("-----  table2")
##[print(table2[j]) for j in range(10)]
###################################################
###################################################

## 2.
import random
tmp1=[i for i in range(1,101)]
tmp2=[j for j in range(101,201)]

for i in range (0,10):
    for j in range (0,10):
        if len(tmp1)!=1:
            table1[i][j]=tmp1.pop(random.randrange(0,len(tmp1)-1))
        else:
            table1[i][j]=tmp1[0]
        if len(tmp2)!=1:
            table2[i][j]=tmp2.pop(random.randrange(0,len(tmp2)-1))
        else:
            table2[i][j]=tmp2[0]

print("\n------ 2. 랜덤 ------")
[print(table1[i]) for i in range(10)]
[print(table2[j]) for j in range(10)]
        
###################################################
###################################################

## 3.
k,l=0,0
tmp=0
for i in range(0,10):
    for j in range(0,10):
        
        if table1[i][j]%2==0:
            tmp=table1[i][j]
            
            while table2[k][l]%2==0:
                l+=1
                if l==10: l=0; k=k+1;
##                print(k,l)
            table1[i][j]=table2[k][l]
            table2[k][l]=tmp
            

print("\n------ 3. 홀수 ------")
[print("%3d"%table1[i][j],end=' ') for i in range(10) for j in range(10)]
print("\n------ 3. 짝수 ------")
[print("%3d"%table2[i][j],end=' ') for i in range(10) for j in range(10)]
##[print(table2[j]) for j in range(10)]




