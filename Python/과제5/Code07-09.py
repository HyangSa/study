#_*_coding=cp949
#_*_coding: euc-kr
## ��ųʸ�
## ��ųʸ��� ����
import operator # �ҷ�����

trainDic, trainList = {}, [] # ��ųʸ�, ����Ʈ ����

trainDic = {'Tomas':'�丶��','Edward':'�������','Henry':'�',
            'Gothen':'���', 'James':'���ӽ�'} # ��ųʸ� Ű, �� ����
trainList = sorted(trainDic.items(), key=operator.itemgetter(0))
# ��ųʸ� ���� �� ����Ʈ�� ����
# key=operator.itemgetter(0) Ű�� ��������
# key=operator.itemgetter(1) ���� ��������

print(trainList) # ����� ���
