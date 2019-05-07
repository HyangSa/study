#_*_coding=cp949
#_*_coding: euc-kr
##중첩 if문
##if~else~if~else문

score = int(input("점수를 입력하세요 : ")) # score 입력받음

if score >= 90 :# score >= 90 일때
    print("A")  # A 출력
else :              # score >= 90이 거짓일때
    if score >= 80 :# score >= 80 일때
        print("B")  # B 출력
    else :              # score >= 80 거짓일때
        if score >= 70 :# score >= 70 일때
            print("C")  # C 출력
        else :              # score >= 70 거짓일때
            if score >= 60 :# score >= 60 일때
                print("D")  # D 출력
            else :              # score >= 60 거짓일때
                print("F")      # F 출력

print("학점입니다. ^^")  #문자열 출력 (if 문에 포함되어있지않다.)
