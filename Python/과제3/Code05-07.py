#_*_coding=cp949
#_*_coding: euc-kr
##��ø if��
##if~else~if~else��

score = int(input("������ �Է��ϼ��� : ")) # score �Է¹���

if score >= 90 :# score >= 90 �϶�
    print("A")  # A ���
else :              # score >= 90�� �����϶�
    if score >= 80 :# score >= 80 �϶�
        print("B")  # B ���
    else :              # score >= 80 �����϶�
        if score >= 70 :# score >= 70 �϶�
            print("C")  # C ���
        else :              # score >= 70 �����϶�
            if score >= 60 :# score >= 60 �϶�
                print("D")  # D ���
            else :              # score >= 60 �����϶�
                print("F")      # F ���

print("�����Դϴ�. ^^")  #���ڿ� ��� (if ���� ���ԵǾ������ʴ�.)
