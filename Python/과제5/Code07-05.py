#_*_coding=cp949
#_*_coding: euc-kr
## ����Ʈ�� �⺻
## ����Ʈ ���� �Լ�
myList = [30,10,20] # ����Ʈ ����
print("���� ����Ʈ : %s" %myList) # ����Ʈ �� ���

myList.append(40) # ����Ʈ�� �� 40 �߰�
print("append(40) ���� ����Ʈ : %s" %myList) # ����Ʈ ���

print("pop()���� ������ �� : %s" %myList.pop()) # ����Ʈ���� �� �� ���� �� ���
print("pop() ���� ����Ʈ : %s" %myList) # �� ���� ���� �� ����Ʈ ���

myList.sort() # ����Ʈ �׸� ����
print("sort() ���� ����Ʈ : %s" %myList) # ���ĵ� ����Ʈ �� ���

myList.reverse() # ����Ʈ �������� ����
print("reverse() ���� ����Ʈ : %s" %myList) # �������� �ٲ� ����Ʈ ���

print("20���� ��ġ : %d" %myList.index(20)) # 20���� ��ġ ���

myList.insert(2,222) # ����Ʈ 2�� ��ġ�� 222 �߰�
print("insert(2,222) ���� ����Ʈ : %s" %myList) # 222�߰��� ����Ʈ ���

myList.remove(222) # �� 222 ����
print("remove(222) ���� ����Ʈ : %s" %myList) # 222���� ���� ����Ʈ ���

myList.extend([77,88,77]) # ����Ʈ�ڿ� �Է��� ����Ʈ �߰�
print("extend([77,88,77]) ���� ����Ʈ : %s" %myList) # ����Ʈ�� �߰��� ����Ʈ ���

print("77���� ���� : %d" %myList.count(77)) # ����Ʈ�� 77�� �� ���� ���
