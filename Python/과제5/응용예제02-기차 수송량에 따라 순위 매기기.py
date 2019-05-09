#_*_coding=cp949
#_*_coding: euc-kr
## 응용예제02
## 기차 수송량에 따라 순위 매기기
import operator # operator 불러오기

## 변수 선언 부분 ##
trainTupleList=[('토마스',5),('헨리',8),('에드웓',9),('에밀리',5),
                ('토마스',4),('헨리',7),('토마스',3),('에밀리',8),
                ('퍼시',5),('고든',13)] # 튜플리스트 선언
trainDic,trainList={},[] # 딕셔너리 리스트 선언
tmpTup=None # 임시 변수 선언
totalRank,currentRank=1,1 # 전체 순위, 동일한 순위(현재순위) 변수 선언(초기화)
## 메인 코드 부분 ##
if __name__=="__main__":
    for tmpTup in trainTupleList: # 리스트 값 순서대로 반복
        tName=tmpTup[0] # 이름=리스트 1번째 값 대입
        tWeight=tmpTup[1] # 무게=리스트 2번째 값 대입
        if tName in trainDic: # 대입된 이름이 딕셔너리에 있다면
            trainDic[tName]+=tWeight # 딕셔너리의 동일한 키에 해당하는 값에 무게 추가
        else : # 그 외에는
            trainDic[tName]=tWeight # 새로운 값 등록

    print("기차 수송량 목록 ==> ", trainTupleList) # 리스트 값 출력 
    print("---------------------------") # 점선 출력
    trainList=sorted(trainDic.items(),key=operator.itemgetter(1),reverse=True)
    # 딕셔너리 값 순서별로 정렬 및 순서 반전 후 리스트에 대입
    print("기차\t총 수송량\t순위") # 내용 출력
    print("---------------------------") # 점선 출력
    print(trainList[0][0],'\t',trainList[0][1],'\t\t',currentRank)
    # 리스트의 첫번째 출력(1위 우선 출력)
    for i in range(1,len(trainList)): # 1~리스트 길이까지 반복
        totalRank+=1 # 전체 순위 1 증가
        if trainList[i][1]==trainList[i-1][1] : # 앞기차의 무게와 현재 기차의 무게가 같다면
            pass # if문 pass
        else : # 그렇지 않다면
            currentRank=totalRank #현재 등수에 전체 등수 대입
        print(trainList[i][0],'\t',trainList[i][1],'\t\t',currentRank)
        # 튜플리스트의 i번째 값과 현재 등수 출력
