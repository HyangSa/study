#_*_coding=cp949
#_*_coding: euc-kr
##
import random # random �ҷ�����

## �Լ� ���� �κ� ##
def getNumber(strData): #�Լ� �̸�, �μ� ����
    numStr='' # ���� ����
    for ch in strData : # �μ��� �Է¹������ڿ� ������� 1���� ch�� ���� ����
        if ch.isdigit(): # ���Ե� ch�� ���ڶ��
            numStr += ch # numStr������ �߰�

    return int(numStr) # numStr���� ���������� ��ȯ

## ���� ���� ���� �κ� ##
data=[] # ����Ʈ�� �������� ����
i,k=0,0 # ���� ���� ����

## ���� �ڵ� �κ� ##
if __name__ == "__main__" :
    for i in range (0, 10): # 0~9���� �ݺ� (10��)
        tmp = hex( random.randrange(0, 100000)) # 0~100000������ ���� 16���� ��
        tmp = tmp[2:]       # ���� 0x ����
        data.append(tmp)    #data����Ʈ�� tmp �� ����

    print('���� �� ������ : ', end = '') # ���� ���
    [print(num, end = ' ') for num in data]
    #(���������) data����Ʈ���� 1���� ������� ���

    for i in range(0, len(data) - 1): # i=0~����Ʈ����-1 ��ŭ �ݺ�
        for k in range(i + 1, len(data)):
            # k=(i+1)~����Ʈ���� ��ŭ �ݺ�(i��° ����Ʈ �� ���� ���� ���ϱ�����)
            if getNumber(data[i]) > getNumber(data[k]): # ������ ���϶�
                # (����Ʈ i��° �� ���ڸ� ���� ������ > ����Ʈ k��° �� ���ڸ� ���� ������)
                tmp = data[i] # �ӽú����� ����Ʈ i��° �� ����
                data[i] = data[k] # ����Ʈ i��°�� k��° �� ����
                data[k] = tmp # ����Ʈ k��°�� �ӽú����� �����س� �� ����

    print('\n���� �� ������ : ', end = '') # ���� ���
    [print(num, end = ' ') for num in data]
    #(���������) data����Ʈ���� 1���� ������� ���
