#_*_coding=cp949
#_*_coding: euc-kr
##��¥ ���� �� ���� ���ϱ�
from time import * # time �ҷ�����
from datetime import * # datetime �ҷ�����
## �Լ� ���� �κ� ##
def countDays(date1,date2): # ��¥ �� ����(�Լ� �̸�, �μ� ����)
    retDays = 0 # ���� ����
    year, month, day = date1.split('/') # '/'�������� ���� ������ ����Ʈ�� ��ȯ
    sDay = date(int(year), int(month), int(day))
    # ������ ���� ���� ������ �Է��Ͽ� date��ü ����
    year, month, day = date2.split('/') # '/'�������� ���� ������ ����Ʈ�� ��ȯ
    eDay = date(int(year), int(month), int(day))
    # ������ ���� ���� ������ �Է��Ͽ� date��ü ����
    diffDays = eDay - sDay # �� ��¥�� �� ���
    retDays = diffDays.days # ��¥�� ����
    return retDays # ����� ��ȯ

def getDay(t):  # ���� ���ϱ�
    weeks = ['��', 'ȭ', '��', '��', '��', '��', '��'] # 0~6 ��~�� ������ ����Ʈ ����
    return weeks[t.tm_wday] # tm_wday�� ����(������~�Ͽ���, 0~6)���� ��ȯ

## ���� ���� ���� �κ� ##
startDate, curDate, tm = '', '', None

## ���� �ڵ� �κ� ##
if __name__ == "__main__" :

    startDate = input('���� ��¥(��/��/��) --> ') #���� ��¥ �Է�
    tm = localtime() # �ý��۱����� ����ð��� struct_time�� tm�� ����
    curDate = str(tm.tm_year)+'/'+str(tm.tm_mon)+'/'+str(tm.tm_mday)
    # tm�������� �޾ƿ� struct_timeŸ���� ��ü���� �⵵/��/�� �������� �Ӽ��� �о�� ����

    print(startDate, '���� ����(',curDate,')������ ', countDays(startDate, curDate), '���� �������ϴ�')
    # startDate, curDate, countDays�Լ��� ����Ͽ� �� ��¥�� ��(�ϼ�) ���
    print('�׸��� ������ ',getDay(tm),'�����Դϴ�')
    # ���� �ð��� �μ��� ����Ͽ� getDay �Լ� ȣ�� - ���� ���
