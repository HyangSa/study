#_*_coding=cp949
#_*_coding: euc-kr
##if문 응용
##리스트와 함께 사용

import random # random 불러오기

numbers = [] # 리스트형 변수 선언
for num in range(0, 10) :
    numbers.append(random.randrange(0, 10))
    #10번 반복하며 0~9 사이의 랜덤한 값을 리스트에 추가

print("생성된 리스트", numbers) #위에서 만든 리스트 출력

for num in range(0, 10) : # 0~9
    if num not in numbers :
        print("숫자 %d는(은) 리스트에 없네요." %num)
        # num이 1씩 증가하면서 numbers 리스트에 같은 수가 없을시 출력
