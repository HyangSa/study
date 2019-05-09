#_*_coding=cp949
#_*_coding: euc-kr
## 리스트의 기본
## 리스트 조작 함수
myList = [30,10,20] # 리스트 선언
print("현재 리스트 : %s" %myList) # 리스트 값 출력

myList.append(40) # 리스트에 값 40 추가
print("append(40) 후의 리스트 : %s" %myList) # 리스트 출력

print("pop()으로 추출한 값 : %s" %myList.pop()) # 리스트에서 뺀 맨 뒤의 값 출력
print("pop() 후의 리스트 : %s" %myList) # 맨 뒤의 값을 뺀 리스트 출력

myList.sort() # 리스트 항목 정렬
print("sort() 후의 리스트 : %s" %myList) # 정렬된 리스트 값 출력

myList.reverse() # 리스트 역순으로 변경
print("reverse() 후의 리스트 : %s" %myList) # 역순으로 바꾼 리스트 출력

print("20값의 위치 : %d" %myList.index(20)) # 20값을 위치 출력

myList.insert(2,222) # 리스트 2의 위치에 222 추가
print("insert(2,222) 후의 리스트 : %s" %myList) # 222추가한 리스트 출력

myList.remove(222) # 값 222 삭제
print("remove(222) 후의 리스트 : %s" %myList) # 222값을 지운 리스트 출력

myList.extend([77,88,77]) # 리스트뒤에 입력한 리스트 추가
print("extend([77,88,77]) 후의 리스트 : %s" %myList) # 리스트가 추가된 리스트 출력

print("77갑의 개수 : %d" %myList.count(77)) # 리스트에 77인 값 개수 출력
