#_*_coding=cp949
#_*_coding: euc-kr
## 2���� ����Ʈ
## 2���� ����Ʈ�� ����
list1=[] # ����Ʈ1 ����
list2=[] # ����Ʈ2 ����
value=1 # �� �ʱ�ȭ(1)
for i in range(0,3): # i:0~2 ���� �ݺ�
    for k in range(0,4): # k:0~3���� �ݺ�
        list1.append(value) # ����Ʈ1�� �� �߰�
        value+=1 # ��=1�� ����
    list2.append(list1) # ����Ʈ2�� ����Ʈ1 �߰�(i:0~2���� �ݺ��� ����)
    list1=[] # ����Ʈ1 �ʱ�ȭ
#3�� 4��¥�� ����Ʈ �ۼ� �Ϸ�
for i in range(0,3): # 0~2���� �ݺ�
    for k in range(0,4): # 0~3���� �ݺ�
        print("%3d" %list2[i][k], end="") # list2[0][0]~list[2][3]���� ���
    print("") # k�� 0~3���� �� �� �ٹٲ�(i�� �ݺ����� ����)
