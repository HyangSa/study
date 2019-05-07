#_*_coding=cp949
#_*_coding: euc-kr
## while문
## 무한 루프를 하는 while문
ch="" # 입력받을 변수 선언
a,b=0,0 # 입력받을 변수 선언

while True : # 무한반복
    a = int(input("계산할 첫 번째 수를 입력하세요 : ")) # a 입력
    b = int(input("계산할 두 번째 수를 입력하세요 : ")) # b 입력
    ch = input("계산할 연산자를 입력하세요 : ")         # ch 입력(연산자)

    if (ch == "+") :    # ch 가 +일때
        print("%d + %d = %d" % (a, b, a + b))   # a+b 결과 출력
    elif (ch == "-") :  # ch 가 -일때
        print("%d - %d = %d" % (a, b, a - b))   # a-b 결과 출력
    elif (ch == "*") :  # ch 가 *일때
        print("%d * %d = %d" % (a, b, a * b))   # a*b 결과 출력
    elif (ch == "/") :  # ch 가 /일때
        print("%d / %d = %5.2f" % (a, b, a / b))# a/b 결과 출력
    elif (ch == "%") :  # ch 가 %일때
        print("%d %% %d = %d" % (a, b, a % b))  # a%b 결과 출력
    elif (ch == "//") : # ch 가 //일때
        print("%d // %d = %d" % (a, b, a // b)) # a//b 결과 출력
    elif (ch == "**") : # ch 가 **일때
        print("%d ** %d = %d" % (a, b, a ** b)) # a**b 결과 출력
    else : # ch 가 그 외 일때
        print("연산자를 잘못 입력했습니다") # 내용 출력
