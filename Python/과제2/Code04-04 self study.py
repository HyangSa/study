#_*_coding=cp949
#_*_coding: euc-kr
##��Ʈ ������
##����Ʈ ������

result=0

a=int(input("����Ʈ�� ���ڴ�? "))
count=int(input("����� Ƚ����? "))

for i in range(1,count+1):
    result = a << i
    print("%d << %d = %d" % (a,i,result)) 

for i in range(1,count+1):
    result = a >> i
    print("%d >> %d = %d" % (a,i,result)) 
