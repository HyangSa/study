#_*_coding=cp949
#_*_coding: euc-kr
##break���� continue��
##�ݺ����� Ż���Ű�� break��
hap, i = 0,0 # ���� ����

for i in range(1,101): # i = 1~100���� �ݺ�
    hap += i # i ��ø

    if hap >= 1000 : # i��ø��(hap)�� 1000���� ���ų� Ŭ ���
        break # while�� Ż�� 

print("1~100�� �հ踦 ���ʷ� 1000�� �Ѱ� �ϴ� ���� : %d" % i)
# ��ø���� 1000�� �Ѿ�����(while�� Ż�� ��) i�� �� ���
