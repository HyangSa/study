#_*_coding=cp949
#_*_coding: euc-kr
##
## ���뿹��01 - ��Ʈ��� �����
## ���� ���� �κ� ##
i, k, heartNum = 0,0,0           # ���� ����
numStr, ch, heartStr = "", "", ""# ���� ����

## ���� �ڵ� �κ� ##
if __name__ == "__main__" :
    numStr = input("���ڸ� ���� �� �Է��ϼ��� : ") #numStr �Է�
    print("") # ���� �ٹٲ� ���
    i = 0     # i�� �ʱ�ȭ
    ch = numStr[i] #ch�� numStr���ڿ��� ù��°�� ����
    while True :                        # ���� �ݺ�
         heartNum = int(ch)             # heartNum�� ch�� ���������� ����
         heartStr = ""                  # heartStr �ʱ�ȭ
         
         for k in range (0, heartNum):  # k(0)~heartNum��ŭ �ݺ�
              heartStr += "\u2665"      # heartStr�� ��Ʈ��� ��ø(heartNum��ŭ)
              k += 1                    # k�� 1����
		
         print(heartStr)                # heartStr(��ø�� ��Ʈ���) ���

         i += 1                         # i�� 1 ����
         
         if (i > len(numStr)-1) :       # i���� �Է¹��� numStr���ڿ�����-1���� ũ��
              break                     # while�� Ż��

         ch = numStr[i]                 # ch�� numStr���ڿ��� ������ ����(i+=1)
    
