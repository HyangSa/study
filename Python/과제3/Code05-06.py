#_*_coding=cp949
#_*_coding: euc-kr
##중첩 if문
##if~else~if~else문

a = 75 # a에 75 대입

if a > 50 : # a > 50 이 참일때 if문에 포함된 코드 실행
    if a < 100 :
        print("50보다 크고 100보다 작군요.") #  a < 100 참일때 (50<a<100)
    else :
        print("와~~ 100보다 크군요") # a < 100 거짓일때
else :  
    print("에고~ 50보다 작군요.") # a > 50 거짓일때

