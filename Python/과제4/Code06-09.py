#_*_coding=cp949
#_*_coding: euc-kr
## while문
## for문과 while문 비교
i, hap = 0, 0 # 변수선언

i = 1 # i에 1 대입
while i < 11 :      # i < 11가 참일 경우 반복 (i=10까지 증가)
    hap = hap + i  # i값 중첩
    i = i + 1      # i 1씩 증가

print("1에서 10까지의 합계 : %d" % hap) # 결과 출력
