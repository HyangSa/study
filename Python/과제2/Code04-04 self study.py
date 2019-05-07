#_*_coding=cp949
#_*_coding: euc-kr
##비트 연산자
##시프트 연산자

result=0

a=int(input("시프트할 숫자는? "))
count=int(input("출력할 횟수는? "))

for i in range(1,count+1):
    result = a << i
    print("%d << %d = %d" % (a,i,result)) 

for i in range(1,count+1):
    result = a >> i
    print("%d >> %d = %d" % (a,i,result)) 
