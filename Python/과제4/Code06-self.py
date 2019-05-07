#_*_coding=cp949
#_*_coding: euc-kr
## 중첩 for문
## 중첩 for문의 활용
i, k = 0, 0 # 변수 선언(초기화)

for i in range(2, 10, 1) : # i = 2~9까지 1씩 증가하며 반복
    print("## "+str(i)+"단 ##")
    for k in range(1, 10, 1) : # k = 1~9까지 1씩 증가하며 반복
        print("%d X %d = %2d" %(i, k, i * k)) # 결과 출력
    print("")	# 내용 출력(빈줄)
