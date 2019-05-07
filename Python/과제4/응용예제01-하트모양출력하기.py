#_*_coding=cp949
#_*_coding: euc-kr
##
## 응용예제01 - 하트모양 출력하
## 변수 선언 부분 ##
i, k, heartNum = 0,0,0           # 변수 선언
numStr, ch, heartStr = "", "", ""# 변수 선언

## 메인 코드 부분 ##
if __name__ == "__main__" :
    numStr = input("숫자를 여러 개 입력하세요 : ") #numStr 입력
    print("") # 공백 줄바꿈 출력
    i = 0     # i값 초기화
    ch = numStr[i] #ch에 numStr문자열을 첫번째수 대입
    while True :                        # 무한 반복
         heartNum = int(ch)             # heartNum에 ch를 정수형으로 대입
         heartStr = ""                  # heartStr 초기화
         
         for k in range (0, heartNum):  # k(0)~heartNum만큼 반복
              heartStr += "\u2665"      # heartStr에 하트모양 중첩(heartNum만큼)
              k += 1                    # k값 1증가
		
         print(heartStr)                # heartStr(중첩된 하트모양) 출력

         i += 1                         # i값 1 증가
         
         if (i > len(numStr)-1) :       # i값이 입력받은 numStr문자열길이-1보다 크면
              break                     # while문 탈출

         ch = numStr[i]                 # ch에 numStr문자열중 다음수 대입(i+=1)
    
