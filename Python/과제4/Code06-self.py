#_*_coding=cp949
#_*_coding: euc-kr
## ��ø for��
## ��ø for���� Ȱ��
i, k = 0, 0 # ���� ����(�ʱ�ȭ)

for i in range(2, 10, 1) : # i = 2~9���� 1�� �����ϸ� �ݺ�
    print("## "+str(i)+"�� ##")
    for k in range(1, 10, 1) : # k = 1~9���� 1�� �����ϸ� �ݺ�
        print("%d X %d = %2d" %(i, k, i * k)) # ��� ���
    print("")	# ���� ���(����)
