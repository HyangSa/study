#_*_coding=cp949
#_*_coding: euc-kr
## �Լ��� ��ȯ���� �Ű�����
## [���α׷�1]�� �ϼ�
import random # random�ҷ�����

## �Լ� ���� �κ� ##
def getNumber(): # �Լ� �̸� ����
    return random.randrange(1,46) # ��ȯ��=1~46������ ����

## ���� ���� ���� �κ� ##
lotto=[] # �������� ����Ʈ�� ����
num=0 # �������� ����

## ���� �ڵ� �κ� ##
print("** �ζ� ��÷�� �����մϴ�. ** \n") # ���� ���

while True : # ���� �ݺ�
    num = getNumber() #getNumber�� ��ȯ��(1~46������ ����) ����

    if lotto.count(num)==0 : #num���Ե� ���� lotto����Ʈ�� ������ 0�̶��
        lotto.append(num) # lotto����Ʈ�� �߰�

    if len(lotto)>=6 : # lotto����Ʈ ���̰� 6�� ���ų� ũ��
        break # �ݺ� ����(while�� Ż��)

print("��÷�� �ζ� ��ȣ ==> ", end='') # ���� ���(�ٹٲ�X)
lotto.sort()# lotto����Ʈ ���� ����
for i in range(0, 6): # 0~5���� �ݺ�
    print("%d " %lotto[i], end='') # lotto����Ʈ i��° �� ���(�ٹٲ�X)
##[print(n,end=' ') for n in lotto]
