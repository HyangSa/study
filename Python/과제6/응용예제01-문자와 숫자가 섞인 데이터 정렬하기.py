#_*_coding=cp949
#_*_coding: euc-kr
##
import random # random 불러오기

## 함수 선언 부분 ##
def getNumber(strData): #함수 이름, 인수 정의
    numStr='' # 변수 선언
    for ch in strData : # 인수로 입력받은문자열 순서대로 1개씩 ch에 대입 실행
        if ch.isdigit(): # 대입된 ch가 숫자라면
            numStr += ch # numStr변수에 추가

    return int(numStr) # numStr변수 정수형으로 반환

## 전역 변수 선언 부분 ##
data=[] # 리스트형 전역변수 선언
i,k=0,0 # 전역 변수 선언

## 메인 코드 부분 ##
if __name__ == "__main__" :
    for i in range (0, 10): # 0~9까지 반복 (10번)
        tmp = hex( random.randrange(0, 100000)) # 0~100000사이의 난수 16진수 대
        tmp = tmp[2:]       # 앞의 0x 제거
        data.append(tmp)    #data리스트에 tmp 값 대입

    print('정렬 전 데이터 : ', end = '') # 내용 출력
    [print(num, end = ' ') for num in data]
    #(컴프리헨션) data리스트에서 1개씩 순서대로 출력

    for i in range(0, len(data) - 1): # i=0~리스트길이-1 만큼 반복
        for k in range(i + 1, len(data)):
            # k=(i+1)~리스트길이 만큼 반복(i번째 리스트 뒤 값들 전부 비교하기위함)
            if getNumber(data[i]) > getNumber(data[k]): # 조건이 참일때
                # (리스트 i번째 값 숫자만 뽑은 정수값 > 리스트 k번째 값 숫자만 뽑은 정수값)
                tmp = data[i] # 임시변수에 리스트 i번째 값 대입
                data[i] = data[k] # 리스트 i번째에 k번째 값 대입
                data[k] = tmp # 리스트 k번째에 임시변수에 대입해논 값 대입

    print('\n정렬 후 데이터 : ', end = '') # 내용 출력
    [print(num, end = ' ') for num in data]
    #(컴프리헨션) data리스트에서 1개씩 순서대로 출력
