#_*_coding=cp949
#_*_coding: euc-kr
## ���뿹��01
## 16���� ����
import random # ���� �ҷ�����

## ���� ���� �κ� ##
data=[] # data ����Ʈ ����
i,k=0,0 # ���� 2�� ����(�ʱ�ȭ)
## ���� �ڵ� �κ� ##
if __name__=="__main__":
    for i in range(0,10): # 0~9���� �ݺ�(10��)
        tmp=hex(random.randrange(0,100000)) # 0~100000������ ���� 16���� tmp�� ����
        data.append(tmp) # data����Ʈ�� 16���� ���߰�

    print("���� �� ������: ", end='') # ���� ���
    [print(num,end=' ') for num in data] #(���������) ����Ʈ �� ���

    for i in range(0, len(data)-1): # 0~data����-1���� �ݺ�(0~9)
        for k in range(i+1, len(data)): # i+1~9���� �ݺ�(i�� �����Կ����� Ƚ��-1)
            if int(data[i],16) > int(data[k], 16):
                #������ ����Ʈ�� i��° ������ > �����͸���Ʈ�� k��° �������� ���̸�
                tmp=data[i] # �ӽ� ������ ����Ʈ�� i��° �� ����
                data[i]=data[k] # ����Ʈ i��° ��ġ�� ����Ʈ�� k��° �� ����
                data[k]=tmp # ����Ʈ k��° ��ġ�� ���� ������ ���� i��° �� ����

    print("\n���� �� ������: ", end='') # ���� ���
    [print(num,end=' ') for num in data] #(���������) ����Ʈ �� ���
