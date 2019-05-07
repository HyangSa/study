#_*_coding=cp949
#_*_coding: euc-kr
##데이터 표현 단위와 진수 변환
##[프로그램2]의 완성
sel = int(input("입력 진수 결정(16/10/8/2) : ")) #정수형으로 입력될 진수 결정
num = input("값 입력 : ") # 숫자 입력

if sel == 16 : # 입력받은 sel가 16일 경우
    num10=int(num,16) # 16진수를 10진수로
if sel == 10 : # 입력받은 sel가 10일 경우
    num10=int(num,10) # 10진수를 10진수로
if sel == 8 : # 입력받은 sel가 8일 경우
    num10=int(num,8)  # 8진수를 10진수로
if sel == 2 : # 입력받은 sel가 2일 경우
    num10=int(num,2)  # 2진수를 10진수로

print("16진수 ==> ",hex(num10)) #16진수로 출력
print("10진수 ==> ",num10)      #10진수로 출력
print(" 8진수 ==> ",oct(num10)) #8진수로 출력
print(" 2진수 ==> ",bin(num10)) #2진수로 출력
