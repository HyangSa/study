import pdb
################       TIC     ###################
import time
t=time.time() # t= 컴퓨터 현제 시각

## 5. 버블정렬 (11%4=3)
sentence=('Twinkle, twinkle, little star,\
How I wonder what you are.\
Up above the world so high,\
Like a diamond in the sky.\
When the blazing sun is gone,\
When he nothing shines upon,\
Then you show your little light,\
Twinkle, twinkle, all the night.\
Then the traveler in the dark,\
Thank you for your tiny spark,\
He could not see which way to go,\
If you did not twinkle so.\
In the dark blue sky you keep,\
And often through my curtains peep,\
For you never shut your eye,\
Till the sun is in the sky.\
As your bright and tiny spark,\
Lights the traveler in the dark.\
Though I know not what you are,\
Twinkle, twinkle, little star.\
Twinkle, twinkle, little star.\
How I wonder what you are.\
Up above the world so high,\
Like a diamond in the sky.\
Twinkle, twinkle, little star.\
How I wonder what you are.\
How I wonder what you are.')
##re=sentence.split()
re=[] #빈 리스트 생성
[re.append(sentence[i]) for i in range(0,len(sentence))] #문자 1개씩 리스트에 추가
##print(re)

def bubbleSort(x): # 버블정렬 함수 정의
    size=len(x) # 리스트 크기
    for i in range(size-1,0,-1): # i=리스트 뒤부터 앞으로 
        for j in range(0,i): # j=리스트 0부터 i까지.
##            print(i,j)
            if x[j]>x[j+1]: # 리스트j째 값이 앞의 값보다 크면
                tmp=x[j]    # 임시변수에 j번째 값을 넣고
                x[j]=x[j+1] # j번째에 앞의 값을 넣고
                x[j+1]=tmp  # 임시변수에 저장한 j번째였던 값을 앞에 입력
            # 앞에서부터 큰 값을 맨 오른쪽으로 빼줌
    return x # 정렬된 리스트 반환

re=bubbleSort(re) # 정렬한 리스트 값 re에 대입
result='' # 빈 문자열 변수
for i in range(0,len(re)): # i=0~리스트 크기-1만큼
    result+=re[i] # 결과값에 리스트값 1개씩 중첩
# 결과는 정렬된 리스트 값을 1개씩 끝까지 뽑아낸 문자열
print(result) # 결과 출력

elapsed = time.time() - t # 경과한 시간은 현재시각 - t(프로그램시작시 시간)
print(elapsed) # 경과한 시간 출력
