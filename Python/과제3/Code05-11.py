#_*_coding=cp949
#_*_coding: euc-kr
##if�� ����
##[���α׷� 2]�� �ϼ�

## ���� ���� �κ� ##
select, answer, numStr, num1, num2 = 0, 0, "", 0, 0 # �� ���� ����

## ���� �ڵ� �κ� ##
select = int(input("1. �Է��� ���� ��� 2. �� �� ������ �հ� : ")) # select �Է�

if select ==1 : # �Էµ� select�� 1�϶�
    numStr = input("*** ������ �Է��ϼ��� : ") # numStr �Է�
    answer = eval(numStr) # �Է¹��� ���� ���
    print("%s ����� %5.1f�Դϴ�." %(numStr, answer)) # ��� ���
elif select == 2 :  # �Էµ� select�� 2�϶�
    num1 = int(input("*** ù ��° ���ڸ� �Է��ϼ��� : ")) # num1 �Է�
    num2 = int(input("*** �� ��° ���ڸ� �Է��ϼ��� : ")) # num2 �Է�
    for i in range(num1,num2+1): # num1 ���� 1�� num2���� ����
        answer = answer + i      # num1 ���� num2���� 1�� �����ϴ� i�� ��� ����(��ø)
    print("%d+...+%d�� %d�Դϴ�." %(num1, num2, answer)) # ��� ���
else:   # �Էµ� select�� 1�̳� 2�� �ƴҽ� ��� 
    print("1 �Ǵ� 2�� �Է��ؾ� �մϴ�.") # ���� ���
