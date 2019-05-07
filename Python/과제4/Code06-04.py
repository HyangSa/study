#_*_coding=cp949
#_*_coding: euc-kr
## 기본 for문
## 키보드로 입력한 값까지 합계 구하기
i, hap = 0, 0 # 변수 선언(초기화)
num = 0 # 변수 선언

num = int(input("값을 입력하세오 : ")) # num 입력

for i in range(1, num+1, 1): # 1~입력받은num까지 1씩증가하면서 반복
    hap = hap + i # i값 중첩
	 
print("1에서 %d까지의 합계 : %d" % (num, hap)) # 결과 출력
