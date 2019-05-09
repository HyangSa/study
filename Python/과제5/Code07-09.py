#_*_coding=cp949
#_*_coding: euc-kr
## 딕셔너리
## 딕셔너리의 정렬
import operator # 불러오기

trainDic, trainList = {}, [] # 딕셔너리, 리스트 선언

trainDic = {'Tomas':'토마스','Edward':'에드워드','Henry':'헨리',
            'Gothen':'고든', 'James':'제임스'} # 딕셔너리 키, 값 대입
trainList = sorted(trainDic.items(), key=operator.itemgetter(0))
# 딕셔너리 정렬 후 리스트에 대입
# key=operator.itemgetter(0) 키를 기준으로
# key=operator.itemgetter(1) 값를 기준으로

print(trainList) # 결과값 출력
