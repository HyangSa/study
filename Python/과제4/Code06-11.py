#_*_coding=cp949
#_*_coding: euc-kr
## while��
## ���� ������ �ϴ� while��
ch="" # �Է¹��� ���� ����
a,b=0,0 # �Է¹��� ���� ����

while True : # ���ѹݺ�
    a = int(input("����� ù ��° ���� �Է��ϼ��� : ")) # a �Է�
    b = int(input("����� �� ��° ���� �Է��ϼ��� : ")) # b �Է�
    ch = input("����� �����ڸ� �Է��ϼ��� : ")         # ch �Է�(������)

    if (ch == "+") :    # ch �� +�϶�
        print("%d + %d = %d" % (a, b, a + b))   # a+b ��� ���
    elif (ch == "-") :  # ch �� -�϶�
        print("%d - %d = %d" % (a, b, a - b))   # a-b ��� ���
    elif (ch == "*") :  # ch �� *�϶�
        print("%d * %d = %d" % (a, b, a * b))   # a*b ��� ���
    elif (ch == "/") :  # ch �� /�϶�
        print("%d / %d = %5.2f" % (a, b, a / b))# a/b ��� ���
    elif (ch == "%") :  # ch �� %�϶�
        print("%d %% %d = %d" % (a, b, a % b))  # a%b ��� ���
    elif (ch == "//") : # ch �� //�϶�
        print("%d // %d = %d" % (a, b, a // b)) # a//b ��� ���
    elif (ch == "**") : # ch �� **�϶�
        print("%d ** %d = %d" % (a, b, a ** b)) # a**b ��� ���
    else : # ch �� �� �� �϶�
        print("�����ڸ� �߸� �Է��߽��ϴ�") # ���� ���
