#_*_coding=cp949
#_*_coding: euc-kr
## ��ø for��
## [���α׷� 1]�� �ϼ�

## ���� ���� ���� �κ� ##
i, k, guguLine = 0, 0, "" #��������

## ���� �ڵ� �κ� ##
for i in range(2, 10) : # 2~9���� �ݺ�
    guguLine = guguLine + (" #  %d��  #" %i) #guguLine = # 2��...9�� #

print(guguLine) # 2��...9�� # ���

for i in range(1, 10) : # 1~9���� �ݺ�
    guguLine = "" # guguLine �ʱ�ȭ
    for k in range(2, 10) : # 2~9���� �ݺ�
        guguLine = guguLine + str("%2d X%2d= %2d" %(k, i, k*i))
        # guguLine = guguLine + k(2~9����) X i(1) = k*i
        # guguLine = guguLine + k(2~9����) X i(2) = k*i
        # guguLine = guguLine + k(2~9����) X i(3) = k*i
        #              ...
        # guguLine = guguLine + k(2~9����) X i(9) = k*i
    print(guguLine) # guguLine ���
