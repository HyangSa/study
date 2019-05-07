#_*_coding=cp949
#_*_coding: euc-kr
##if문 응용
##[프로그램 2]의 완성

## 변수 선언 부분 ##
select, answer, numStr, num1, num2 = 0, 0, "", 0, 0 # 각 변수 선언

## 메인 코드 부분 ##
select = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계 : ")) # select 입력

if select ==1 : # 입력된 select가 1일때
    numStr = input("*** 수식을 입력하세요 : ") # numStr 입력
    answer = eval(numStr) # 입력받은 수식 계산
    print("%s 결과는 %5.1f입니다." %(numStr, answer)) # 결과 출력
elif select == 2 :  # 입력된 select가 2일때
    num1 = int(input("*** 첫 번째 숫자를 입력하세요 : ")) # num1 입력
    num2 = int(input("*** 두 번째 숫자를 입력하세요 : ")) # num2 입력
    for i in range(num1,num2+1): # num1 부터 1씩 num2까지 증가
        answer = answer + i      # num1 부터 num2까지 1씩 증가하는 i을 계속 더함(중첩)
    print("%d+...+%d는 %d입니다." %(num1, num2, answer)) # 결과 출력
else:   # 입력된 select가 1이나 2가 아닐시 출력 
    print("1 또는 2만 입력해야 합니다.") # 내용 출력
