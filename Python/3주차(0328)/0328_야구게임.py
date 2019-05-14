import random as r
a=''
for i in range (0,4):
    a=a+str(r.randrange(0,9))
password=a
s=0; b=0; count=0
while True:
    
    num=input("숫자 추측 : ")

    for i in range(0, 4):
        if num[i] in password :
            b=b+1
##            print("%c 있음 B = %d"%(num[i],b))
    


    if (int(password)//1000==int(num)//1000):
        s=s+1
        b=b-1
    if (int(password)%1000//100==int(num)%1000//100):
        s=s+1
        b=b-1
    if (int(password)%100//10==int(num)%100//10):
        s=s+1
        b=b-1
    if (int(password)%10==int(num)%10):
        s=s+1
        b=b-1
    print("S : %d , B : %d" %(s,b))

    
    if (int(password)//1000==int(num)//1000)and\
       (int(password)%1000//100==int(num)%1000//100)and\
       (int(password)%100//10==int(num)%100//10)and \
       (int(password)%10==int(num)%10):
        print("입력 : %s , 정답 : %s" %(num,password))
        break;

    s=0;    b=0
    if count>30:
        break
    count+=1
