#_*_coding=cp949
#_*_coding: euc-kr
##break���� continue��
##�ݺ����� Ż���Ű�� break��
hap = 0 # ���� ����
a, b = 0, 0 # ���� ����

while True : #���ѹݺ�
    a =input("���� ù ��° ���� �Է��ϼ��� : ") # a �Է�
    if a == '$' : # �Է¹��� a�� �϶�
        break   # while�� Ż��
    b = int(input("���� �� ��° ���� �Է��ϼ��� : ")) # b �Է�
    hap = int(a) + b # �Է¹��� a b ��
    print("%d + %d = %d" % (int(a), b, hap)) # �� ��� ��� (a+b=hap)

print("0�� �Է��� �ݺ����� Ż���߽��ϴ�") #(while�� Ż�� ��) ���� ���
