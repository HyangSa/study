#_*_coding=cp949
#_*_coding: euc-kr
##비트연산자
##비트 논리곱과 비트 논리합 연산자
a=ord('A') #'0b0100 0001'
mask=0x0F  #'0b0000 1111'

print("%x & %x = %x" % (a, mask, a&mask)) # 비트 논리곱
# (0100 0001) & (0000 1111) = 0000 0001(0x01)
print("%X & %X = %X" % (a, mask, a|mask)) # 비트 논리합
# (0100 0001) | (0000 1111) = 0100 1111(0x4F)

mask = ord('a') - ord('A') # 0010 0000(0x20)

#비트 배타적 논리합
b = a^mask # (0100 0001) ^ (0010 0000) = 0110 0001
print("%c ^ %d = %c" % (a, mask, b)) # A ^ mask = a
a = b^mask # (0110 0001) ^ (0010 0000) = 0100 0001
print("%c ^ %d = %c" % (b, mask, a)) # a ^ mask = A
