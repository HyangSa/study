#_*_coding=cp949
#_*_coding: euc-kr
##
## ���뿹�� 01 - �ֻ��� ���� ���� ���ÿ� ������
import random

## ���� ���� ���� �κ� ##
dice1, dice2, dice3, dice4, dice5, dice6 = [0]*6    # �� ���� ����
throwCount, serialCount, serialCountcapy = 0, 0, 0  # �� ���� ����

## ���� �ڵ� �κ� ##
if __name__ == "__main__" :
    while True : # ���� �ݺ�
        throwCount += 1     # �ݺ��ɶ����� throwCount 1����

        dice1 = random.randrange(1,7) #
        dice2 = random.randrange(1,7) #
        dice3 = random.randrange(1,7) # �� 6���� �ֻ�����
        dice4 = random.randrange(1,7) # 1~6������ ���� ����
        dice5 = random.randrange(1,7) #
        dice6 = random.randrange(1,7) #

        if dice1==dice2==dice3==dice4==dice5==dice6 : #�ֻ��� 6�� ��� ���� �����ϰ��
            print('6���� �ֻ����� ��� ����ȯ ���ڰ� ���� -->',dice1, dice2, dice3,
                  dice4, dice5, dice6) # �������
            break # while�� Ż��
        elif (dice1==1 or dice2==1 or dice3==1 or dice4==1 or dice5==1 or dice6==1)and\
             (dice1==2 or dice2==2 or dice3==2 or dice4==2 or dice5==2 or dice6==2)and\
             (dice1==3 or dice2==3 or dice3==3 or dice4==3 or dice5==3 or dice6==3)and\
             (dice1==4 or dice2==4 or dice3==4 or dice4==4 or dice5==4 or dice6==4)and\
             (dice1==5 or dice2==5 or dice3==5 or dice4==5 or dice5==5 or dice6==5)and\
             (dice1==6 or dice2==6 or dice3==6 or dice4==6 or dice5==6 or dice6==6) :
            serialCount += 1 # �ֻ��� 6�� ���ڰ� 1~6 ���� Ȯ�� ������ serialCount 1 ����
##        if (dice1 != dice2) and (dice1 != dice3) and (dice1 != dice4) and (dice1 != dice5) and\
##           (dice1 != dice6) and (dice2 != dice3) and (dice2 != dice4) and (dice2 != dice5) and\
##           (dice2 != dice6) and (dice3 != dice4) and (dice3 != dice5) and (dice3 != dice6) and\
##           (dice4 != dice5) and (dice4 != dice6) and (dice5 != dice6) : 
##            serialCountcapy += 1 # ���� ���(�ٸ����)

    print('6���� ������ ���ڰ� ���� ������ �ֻ����� ���� Ƚ�� -->',throwCount)
    # �ݺ��ɶ����� ������  throwCount ���
    print('6���� ������ ���ڰ� ���� ������, 1~6�� ���ӹ�ȣ�� ���� Ƚ�� -->',serialCount)
    # ���ڰ�1~6 �϶� ������  serialCount ���
##    print('1~6 ���ӹ�ȣ �ٸ� ��� test',serialCountcapy)
            
