#_*_coding=cp949
#_*_coding: euc-kr
## (05)���
## [���α׷�2]�� �ϼ�
import random # random �ҷ�����
from tkinter.simpledialog import * # tkinter.simpledialog �ҷ�����

def getString(): # �Լ� �̸� ����
    retStr = '' # ���� ����
    retStr = askstring('���ڿ� �Է�', '�ź��� �� ���ڿ��� �Է�') #���ڿ� �Է�
    return retStr # �Է¹��� ���ڿ��� ����� ��ȯ

def getRGB(): # �Լ� �̸� ����
    r,g,b = 0,0,0 # ���� ����
    r = random.random() # 0~1���� ���� ����
    g = random.random() # 0~1���� ���� ����
    b = random.random() # 0~1���� ���� ����
    return (r,g,b)  # r,g,b ������ ��ȯ

def getXYAS(sw,sh): # �Լ� �̸�, �μ�(2) ��ȯ
    x,y,angle,size = 0,0,0,0 # ���� ����
    x = random.randrange(-sw / 2, sw / 2) # (-�μ�1/2)~(�μ�1/2) ���� ���� ����
    y = random.randrange(-sh / 2, sh / 2) # (-�μ�2/2)~(�μ�2/2) ���� ���� ����
    angle = random.randrange(0,360) # 0~360 ���� ���� ����
    size = random.randrange(10,50) #10~50 ������ ���� ����
    return [x,y,angle,size] # x,y,angle,size ������ ��ȯ
