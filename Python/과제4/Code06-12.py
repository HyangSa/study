#_*_coding=cp949
#_*_coding: euc-kr
##break���� continue��
##�ݺ����� Ż���Ű�� break��
hap = 0 # ���� ����
a, b = 0, 0 # ���� ����

while True : #���ѹݺ�
    a = int(input("���� ù ��° ���� �Է��ϼ��� : ")) # a �Է�
    if a == 0 : # �Է¹��� a�� �϶�
        break   # while�� Ż��
    b = int(input("���� �� ��° ���� �Է��ϼ��� : ")) # b �Է�
    hap = a + b # �Է¹��� a b ��
    print("%d + %d = %d" % (a, b, hap)) # �� ��� ��� (a+b=hap)

print("0�� �Է��� �ݺ����� Ż���߽��ϴ�") #(while�� Ż�� ��) ���� ���
