#_*_coding=cp949
#_*_coding: euc-kr
## ���뿹��02
## ���� ���۷��� ���� ���� �ű��
import operator # operator �ҷ�����

## ���� ���� �κ� ##
trainTupleList=[('�丶��',5),('�',8),('����d',9),('���и�',5),
                ('�丶��',4),('�',7),('�丶��',3),('���и�',8),
                ('�۽�',5),('���',13)] # Ʃ�ø���Ʈ ����
trainDic,trainList={},[] # ��ųʸ� ����Ʈ ����
tmpTup=None # �ӽ� ���� ����
totalRank,currentRank=1,1 # ��ü ����, ������ ����(�������) ���� ����(�ʱ�ȭ)
## ���� �ڵ� �κ� ##
if __name__=="__main__":
    for tmpTup in trainTupleList: # ����Ʈ �� ������� �ݺ�
        tName=tmpTup[0] # �̸�=����Ʈ 1��° �� ����
        tWeight=tmpTup[1] # ����=����Ʈ 2��° �� ����
        if tName in trainDic: # ���Ե� �̸��� ��ųʸ��� �ִٸ�
            trainDic[tName]+=tWeight # ��ųʸ��� ������ Ű�� �ش��ϴ� ���� ���� �߰�
        else : # �� �ܿ���
            trainDic[tName]=tWeight # ���ο� �� ���

    print("���� ���۷� ��� ==> ", trainTupleList) # ����Ʈ �� ��� 
    print("---------------------------") # ���� ���
    trainList=sorted(trainDic.items(),key=operator.itemgetter(1),reverse=True)
    # ��ųʸ� �� �������� ���� �� ���� ���� �� ����Ʈ�� ����
    print("����\t�� ���۷�\t����") # ���� ���
    print("---------------------------") # ���� ���
    print(trainList[0][0],'\t',trainList[0][1],'\t\t',currentRank)
    # ����Ʈ�� ù��° ���(1�� �켱 ���)
    for i in range(1,len(trainList)): # 1~����Ʈ ���̱��� �ݺ�
        totalRank+=1 # ��ü ���� 1 ����
        if trainList[i][1]==trainList[i-1][1] : # �ձ����� ���Կ� ���� ������ ���԰� ���ٸ�
            pass # if�� pass
        else : # �׷��� �ʴٸ�
            currentRank=totalRank #���� ����� ��ü ��� ����
        print(trainList[i][0],'\t',trainList[i][1],'\t\t',currentRank)
        # Ʃ�ø���Ʈ�� i��° ���� ���� ��� ���
