
####  정수 배열과 정수 k가 주어지면 모든 원소를 k칸씩 앞으로 옮기시오.
####  input: [1, 2, 3, 4, 5], k=2
####  output: [3, 4, 5, 1, 2]
####
####  input: [0, 1, 2, 3, 4], k=1
####  output: [1, 2, 3, 4, 0]

def reple(v,k):
    result=[]
    front=v[0:k]
    front.reverse()
    back=v[k:len(v)]
    back.reverse()
    result=front+back
    result.reverse()
    return print(result)

##  1) 첫번째 k원소를 거꾸로 합니다.
##  Time Complexity: O(k) ~= O(n)
##
##  arr: [3, 2, 1, 4, 5, 6, 7]
##
##  2) 나머지 원소들을 거꾸로 합니다.
##  Time Complexity: O(k) ~= O(n)
##
##  arr: [3, 2, 1, 7, 6, 5, 4]
##
##  3) 배열 전체를 거꾸로 합니다.
##  Time Complexity: O(k) ~= O(n)
