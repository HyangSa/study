#_*_coding=cp949
#_*_coding: euc-kr
## 기본 for문
## 키보드로 입력한 값까지 합계 구하기
i, dan = 0, 0 # 변수 선언(초기화)

dan = int(input("단을 입력하세요 : ")) # dan 입력

for i in range(1, 10, 1): # i= 1~9까지 1씩 증가하면서 반복
    print("%d  X  %d  =  %2d" % (dan, i, dan * i))
    # dan X i = dan*i 형식의 결과 출력
