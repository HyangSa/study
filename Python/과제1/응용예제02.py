#_*_coding=cp949
#_*_coding: euc-kr
##변수와데이터형
##응용예제02 입력 문자열을 거꾸로 출력하기

## 변수 선언 부분 ##
inStr=''    #문자열 변수 선언

## 메인 코드 부분 ##
if __name__=='__main__':
    inStr = input('문자열을 입력 -->')    # 문자열 입력

    for i in range(len(inStr) -1, -1, -1) : # (문자열 길이-1)=마지막문자위치
        print('%c' %inStr[i], end='')       # 위치 -1씩 이동하면서 문자 출력
                                            # 0까지 반복실행
