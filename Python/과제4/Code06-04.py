#_*_coding=cp949
#_*_coding: euc-kr
## �⺻ for��
## Ű����� �Է��� ������ �հ� ���ϱ�
i, hap = 0, 0 # ���� ����(�ʱ�ȭ)
num = 0 # ���� ����

num = int(input("���� �Է��ϼ��� : ")) # num �Է�

for i in range(1, num+1, 1): # 1~�Է¹���num���� 1�������ϸ鼭 �ݺ�
    hap = hap + i # i�� ��ø
	 
print("1���� %d������ �հ� : %d" % (num, hap)) # ��� ���
