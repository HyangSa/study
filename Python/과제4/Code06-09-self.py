#_*_coding=cp949
#_*_coding: euc-kr
## �⺻ for��
## Ű����� �Է��� ������ �հ� ���ϱ�
i, hap = 0, 0 # ���� ����(�ʱ�ȭ)
num1, num2, num3 = 0, 0, 0 # �Է¹��� ���� ����

num1 = int(input("���۰��� �Է��ϼ��� : ")) # num1 �Է�
num2 = int(input(" �� ���� �Է��ϼ��� : ")) # num2 �Է�
num3 = int(input("�������� �Է��ϼ��� : ")) # num3 �Է�

##for i in range(num1, num2+1, num3): # i = num1~num2���� num3��ŭ�� ����
##    hap = hap + i # i�� ��ø
i=num1
while i<=num2 :
    hap = hap + i
    i=i+num3
print("%d���� %d���� %d�� ������Ų ���� �հ� : %d" % (num1, num2, num3, hap))
# ��� ���
