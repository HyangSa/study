#_*_coding=cp949
#_*_coding: euc-kr
## (05)���
## [���α׷�2]�� �ϼ�
from myTurtle import * # myTurtle.py �ҷ�����
import turtle # turtle �ҷ�����

## ���� ���� ���� �κ� ##
inStr=''# ���� ���� ����
swidth,sheight = 300,300 # ����� ����� ���� ����
tX,tY,tAngle,txtSize = [0]*4 # ��ǥ��,����,����ũ�� ���� �ʱ�ȭ

## ���� �ڵ� �κ� ##
turtle.title('�ź��� ���ھ���(������)') # �׷��� â �̸� ����
turtle.shape('turtle') # �ź��� ��� ����
turtle.setup(width = swidth + 50, height = sheight + 50) # �׷��� â ũ�� ����
turtle.screensize(swidth, sheight) # �˹����� ũ�� ����
turtle.penup() # ��ø���
turtle.speed(5) # �ź��� �ӵ� ����(5)

inStr=getString() # myTurtle�� getString �Լ� ����(��ȯ�� ����)

for ch in inStr : # inStr�� ������� ch�� �����Ͽ� ����
    
    tX,tY,tAngle,txtSize = getXYAS(swidth, sheight)
    # myTurtle�� getXYAS �Լ� ���� (��ȯ�� ����: tX,tY,tAngle,txtSize=[x,y,angle,size])
    r,g,b = getRGB()  # myTurtle�� getRGB �Լ� ���� r,g,b�� ��ȯ�� ����

    turtle.goto(tX,tY) # �ź��� ��ǥ �̵�
    turtle.left(tAngle) # �ź��� ���� ȸ��(����)

    turtle.pencolor((r,g,b)) # ���Ե� r,g,b ������ �ź��� ���� ����
    turtle.write(ch, font=('�������', txtSize, 'bold')) # inStr���� ���Թ��� ch ���� ����
				
turtle.done() # â ����

