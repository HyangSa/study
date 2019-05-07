#_*_coding=cp949
#_*_coding: euc-kr
##중첩 if문
##if~elif~else문

score = int(input("점수를 입력하세요 : ")) # score 입력받음

if score >= 95 :# score >= 90 일때
    print("A+" ,end =" ")  # A 출력
elif score >= 90 :# score >= 80 일때
    print("A0" ,end =" ")    # B 출력
elif score >= 85 :# score >= 80 일때
    print("B+" ,end =" ")    # B 출력
elif score >= 80 :# score >= 80 일때
    print("B0" ,end =" ")    # B 출력
elif score >= 75 :# score >= 70 일때
    print("C+" ,end =" ")    # C 출력
elif score >= 70 :# score >= 70 일때
    print("C0" ,end =" ")    # C 출력
elif score >= 65 :# score >= 60 일때
    print("D+" ,end =" ")    # D 출력
elif score >= 60 :# score >= 60 일때
    print(str(score)+" : D0" ,end =" ")    # D 출력
else :              # score >= 90,80,70,60 거짓일때
    print("F")      # F 출력

print("학점입니다. ^^")  #문자열 출력 (if 문에 포함되어있지않다.)
