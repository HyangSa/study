#_*_coding=cp949
#_*_coding: euc-kr
## 기본 for문
## 키보드로 입력한 값까지 합계 구하기
i, hap = 0, 0 # 변수 선언(초기화)
num1, num2, num3 = 0, 0, 0 # 입력받을 변수 선언

num1 = int(input("시작값을 입력하세요 : ")) # num1 입력
num2 = int(input(" 끝 값을 입력하세요 : ")) # num2 입력
num3 = int(input("증가값을 입력하세요 : ")) # num3 입력

##for i in range(num1, num2+1, num3): # i = num1~num2까지 num3만큼씩 증가
##    hap = hap + i # i값 중첩
i=num1
while i<=num2 :
    hap = hap + i
    i=i+num3
print("%d에서 %d까지 %d씩 증가시킨 값의 합계 : %d" % (num1, num2, num3, hap))
# 결과 출력
