#_*_coding=cp949
#_*_coding: euc-kr
## while��
## ���� ������ �ϴ� while��
hap = 0 # ���� ����
a, b = 0, 0 # �Է¹��� ���� ����(�ʱ�ȭ)

while True : # ���� �ݺ�
    a = int(input("���� ù ��° ���� �Է��ϼ��� : ")) # a �Է�
    b = int(input("���� �� ��° ���� �Է��ϼ��� : ")) # b �Է�
    hap = a + b # �Է¹��� �μ� ��
    print("%d + %d = %d" % (a, b, hap)) # ��� ��� (a+b=hap)
