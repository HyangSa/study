#_*_coding=cp949
#_*_coding: euc-kr
## �⺻ for��
## Ű����� �Է��� ������ �հ� ���ϱ�
i, dan = 0, 0 # ���� ����(�ʱ�ȭ)

dan = int(input("���� �Է��ϼ��� : ")) # dan �Է�

for i in range(1, 10, 1): # i= 1~9���� 1�� �����ϸ鼭 �ݺ�
    print("%d  X  %d  =  %2d" % (dan, i, dan * i))
    # dan X i = dan*i ������ ��� ���
