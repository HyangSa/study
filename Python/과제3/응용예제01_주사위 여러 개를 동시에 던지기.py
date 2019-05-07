#_*_coding=cp949
#_*_coding: euc-kr
##
## 응용예제 01 - 주사위 여러 개를 동시에 던지기
import random

## 전역 변수 선언 부분 ##
dice1, dice2, dice3, dice4, dice5, dice6 = [0]*6    # 각 변수 선언
throwCount, serialCount, serialCountcapy = 0, 0, 0  # 각 변수 선언

## 메인 코드 부분 ##
if __name__ == "__main__" :
    while True : # 무한 반복
        throwCount += 1     # 반복될때마다 throwCount 1증가

        dice1 = random.randrange(1,7) #
        dice2 = random.randrange(1,7) #
        dice3 = random.randrange(1,7) # 총 6개의 주사위에
        dice4 = random.randrange(1,7) # 1~6사이의 난수 대입
        dice5 = random.randrange(1,7) #
        dice6 = random.randrange(1,7) #

        if dice1==dice2==dice3==dice4==dice5==dice6 : #주사위 6개 모두 같은 숫자일경우
            print('6개의 주사위가 모두 동일환 숫자가 나옴 -->',dice1, dice2, dice3,
                  dice4, dice5, dice6) # 내용출력
            break # while문 탈출
        elif (dice1==1 or dice2==1 or dice3==1 or dice4==1 or dice5==1 or dice6==1)and\
             (dice1==2 or dice2==2 or dice3==2 or dice4==2 or dice5==2 or dice6==2)and\
             (dice1==3 or dice2==3 or dice3==3 or dice4==3 or dice5==3 or dice6==3)and\
             (dice1==4 or dice2==4 or dice3==4 or dice4==4 or dice5==4 or dice6==4)and\
             (dice1==5 or dice2==5 or dice3==5 or dice4==5 or dice5==5 or dice6==5)and\
             (dice1==6 or dice2==6 or dice3==6 or dice4==6 or dice5==6 or dice6==6) :
            serialCount += 1 # 주사위 6개 숫자가 1~6 인지 확인 맞으면 serialCount 1 증가
##        if (dice1 != dice2) and (dice1 != dice3) and (dice1 != dice4) and (dice1 != dice5) and\
##           (dice1 != dice6) and (dice2 != dice3) and (dice2 != dice4) and (dice2 != dice5) and\
##           (dice2 != dice6) and (dice3 != dice4) and (dice3 != dice5) and (dice3 != dice6) and\
##           (dice4 != dice5) and (dice4 != dice6) and (dice5 != dice6) : 
##            serialCountcapy += 1 # 같은 결과(다른방식)

    print('6개가 동일한 숫자가 나올 때까지 주사위를 던진 횟수 -->',throwCount)
    # 반복될때마다 증가한  throwCount 출력
    print('6개가 동일한 숫자가 나올 때까지, 1~6의 연속번호가 나온 횟수 -->',serialCount)
    # 숫자가1~6 일때 증가한  serialCount 출력
##    print('1~6 연속번호 다른 방법 test',serialCountcapy)
            
