#_*_coding=cp949
#_*_coding: euc-kr
## 기본 for문
## for문을 활용한 합계 구하기
i, hap = 0, 0  # 변수 선언(초기화)

for i in range(501, 1001, 2): # i = 501~1000까지 2씩 증가하면서 반복
     hap = hap + i            # hap = i 값 중첩
	
print("500과 1000 사이에 있는 홀수의 합계 : %d" % hap) # 결과 출력
