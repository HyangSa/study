#_*_coding=cp949
#_*_coding: euc-kr
##break문과 continue문
##반복문으로 다시 돌아가게 하는 continue문
hap, i = 0,0 # 변수 선언

for i in range(1,101) : # i = 1~100까지 반복
    if i % 3 == 0 : # i/3의 나머지가 0일때
        continue # for문에 포함된 코드 생략 후 다음 단계 for문 실행
    
    hap += i # i 중첩

print("1~100의 합계(3의 배수 제외): %d" %hap)
# i/3의 나머지가 0일때(3의 배수일때)를 제외한 i의 중첩값 출력
