#_*_coding=cp949
#_*_coding: euc-kr
##��ø if��
##if~elif~else��

score = int(input("������ �Է��ϼ��� : ")) # score �Է¹���

if score >= 95 :# score >= 90 �϶�
    print("A+" ,end =" ")  # A ���
elif score >= 90 :# score >= 80 �϶�
    print("A0" ,end =" ")    # B ���
elif score >= 85 :# score >= 80 �϶�
    print("B+" ,end =" ")    # B ���
elif score >= 80 :# score >= 80 �϶�
    print("B0" ,end =" ")    # B ���
elif score >= 75 :# score >= 70 �϶�
    print("C+" ,end =" ")    # C ���
elif score >= 70 :# score >= 70 �϶�
    print("C0" ,end =" ")    # C ���
elif score >= 65 :# score >= 60 �϶�
    print("D+" ,end =" ")    # D ���
elif score >= 60 :# score >= 60 �϶�
    print(str(score)+" : D0" ,end =" ")    # D ���
else :              # score >= 90,80,70,60 �����϶�
    print("F")      # F ���

print("�����Դϴ�. ^^")  #���ڿ� ��� (if ���� ���ԵǾ������ʴ�.)
