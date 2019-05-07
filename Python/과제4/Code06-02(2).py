#_*_coding=cp949
#_*_coding: euc-kr
## 기본 for문
## for문을 활용한 합계 구하기
i, hap = 0, 0 # 변수 선언(초기화)

for i in range(1, 11, 1):# i = 1~10까지 1씩 증가하면서 반복
        hap = hap + i    # hap = i 값 중첩

print("1에서 10까지의 합계 : %d" %hap) # 결과 내용 출력
