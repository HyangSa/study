#_*_coding=cp949
#_*_coding: euc-kr
##if�� ����
##����Ʈ�� �Բ� ���

import random # random �ҷ�����

numbers = [] # ����Ʈ�� ���� ����
for num in range(0, 10) :
    numbers.append(random.randrange(0, 10))
    #10�� �ݺ��ϸ� 0~9 ������ ������ ���� ����Ʈ�� �߰�

print("������ ����Ʈ", numbers) #������ ���� ����Ʈ ���

for num in range(0, 10) : # 0~9
    if num not in numbers :
        print("���� %d��(��) ����Ʈ�� ���׿�." %num)
        # num�� 1�� �����ϸ鼭 numbers ����Ʈ�� ���� ���� ������ ���
