##for i in range (1,1000):
##    inStr=str(i)
##    if i%6==0 :
##        for j in range(0, len(inStr)):
##            if (inStr[j]=='3') or (inStr[j]=='6') or (inStr[j]=='9') :
##                print("*", end='')
##            else :
##                print("%c" %inStr[j], end='')
##        print("")
##    else :
##        for j in range(0, len(inStr)):
##            if (inStr[j]=='3') or (inStr[j]=='6') or (inStr[j]=='9') :
##                print("*", end='')
##            else :
##                print("%s" %inStr[j], end='')
##        print(" ",end='')
####################################################
"""
다른 방법 : %100 %10 %1 해서 나머지들을 3 6 9 랑 비교후 출력.
"""
temp=''
for i in range (1,1000):
    
    if (i//100==3) or (i//100==6) or (i//100==9):
        #print("*",end='')
        temp=temp+'*'
    else:
        #print(i//100,end='')
        if (i//100==0) : temp=temp+' '
        else : temp=temp+str(i//100)
        
    if (i%100//10==3) or (i%100//10==6) or (i%100//10==9):
        #print("*",end='')
        temp=temp+'*'
    else:
        #print(i%100//10,end='')
        if (i//100==0)and(i%100//10==0) : temp=temp+' '
        else : temp=temp+str(i%100//10)
        
    if (i%10==3) or (i%10==6) or (i%10==9):
        #print("*",end='')
        temp=temp+'*'
    else:
        #print(i%10,end='')
        temp=temp+str(i%10)

    print("%3s " %temp, end='')
    temp=''
    if i%6==0 :
        print("")
