#_*_coding=cp949
#_*_coding: euc-kr
##�����͵�������
##���뿹��01 �������� ũ�� Ȯ���ϱ�
import sys

## ���� ���� �κ� ##
intVar,floatVar,boolVar,strVar,listVar,tupleVar,dicVar,setVar=[None]*8 #�������� 8�� ����


## ���� �ڵ� �κ� ##
if __name__=='__main__':
    intVar=0      # ������ ����
    floatVar=0.0    # �Ǽ��� ������ ����
    boolVar=True    # ���� ������ ����
    strVar=""       # ���ڿ� ������ ����
    listVar=[]      # ����Ʈ�� ������ ����
    tupleVar=()     # Ʃ���� ������ ����
    dicVar={}       # ��ųʸ��� ������ ����
    setVar=set()    # ������ ������ ����

    print('int�� �⺻ ũ�� -->', sys.getsizeof(intVar))       # 
    print('float�� �⺻ ũ�� -->', sys.getsizeof(floatVar))   #
    print('bool�� �⺻ ũ�� -->', sys.getsizeof(boolVar))     # sys.getsizeof() => ũ�⸦ byte������ return
    print('str�� �⺻ ũ�� -->', sys.getsizeof(strVar))       # �� ���������� �⺻ũ�⸦ byte������ ���
    print('list�� �⺻ ũ�� -->', sys.getsizeof(listVar))     #
    print('tuple�� �⺻ ũ�� -->', sys.getsizeof(tupleVar))   #
    print('dictionary�� �⺻ ũ�� -->', sys.getsizeof(dicVar))#
    print('set�� �⺻ ũ�� -->', sys.getsizeof(setVar))       #
