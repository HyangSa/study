#_*_coding=cp949
#_*_coding: euc-kr
## 
## ���뿹�� 02 - �ź��̰� ���� ������ �ϱ�

import turtle # turtle �ҷ�����
import math   # math �ҷ�����
import random # random �ҷ�����

## ���� ���� ���� �κ� ##
t1, t2, t3 = [None] * 3 # �ź��̿� ����� ���� ����
t1X, t1Y, t2X, t2Y, t3X, t3Y = [0] * 6 # X,Y ��ǥ�� ����� ���� ����
swidth, sheight = 300, 300 # ����� ����� ���� ����

## ���� �ڵ� �κ� ##
if __name__ == "__main__" :
    turtle.title('�ź� ������') # �׷��� â �̸� ����
    turtle.setup(width = swidth + 50, height = sheight + 50) # �׷��� â ũ�� ����
    turtle.screensize(swidth, sheight) # �˹����� ũ�� ����
	
    t1 = turtle.Turtle('turtle'); t1.color('red');   t1.penup() # t1�ź��� ����, ����=����, �� �ø���
    t2 = turtle.Turtle('turtle'); t2.color('green'); t2.penup() # t2�ź��� ����, ����=�ʷ�, �� �ø���
    t3 = turtle.Turtle('turtle'); t3.color('blue'); t3.penup()  # t3�ź��� ����, ����=�Ķ�, �� �ø���
	
    t1.goto(-100, -100); t2.goto(0, 0); t3.goto(100, 100) # t1=-100,-100 t2=0,0 t3=100,100 �� ��ǥ�� �̵�
    t1.speed(0); t2.speed(0); t3.speed(0) # �ӵ� ����

    while True : # ���ѹݺ�

        angle = random.randrange(0, 360) # 0~359������ ������ ������ ���
        dist = random.randrange(1, 50)   # 1~49 ������ ������ �Ÿ��� ���
        t1.left(angle); t1.forward(dist) # t1�ź��� �������� ȸ�� �� ����
        angle = random.randrange(0, 360) # 0~359������ ����
        dist = random.randrange(1, 50)   # 1~49 ������ ����
        t2.left(angle); t2.forward(dist) # t2�ź��� �������� ȸ�� �� ����
        angle = random.randrange(0, 360) # 0~359������ ����
        dist = random.randrange(1, 50)   # 1~49 ������ ����
        t3.left(angle); t3.forward(dist) # t3�ź��� �������� ȸ�� �� ����

        t1X = t1.xcor(); t1Y = t1.ycor() # t1�� ���� x,y��ǥ ����
        t2X = t2.xcor(); t2Y = t2.ycor() # t2�� ���� x,y��ǥ ����
        t3X = t3.xcor(); t3Y = t3.ycor() # t3�� ���� x,y��ǥ ����

        if (math.sqrt( ((t1X - t2X)*(t1X - t2X)) + ((t1Y - t2Y)*(t1Y - t2Y)) ) <= 20 or \
            math.sqrt( ((t1X - t3X)*(t1X - t3X)) + ((t1Y - t3Y)*(t1Y - t3Y)) ) <= 20 or \
            math.sqrt( ((t2X - t3X)*(t2X - t3X)) + ((t2Y - t3Y)*(t2Y - t3Y)) ) <= 20) :
            # (t1,t2), (t1,t3), (t2,t3) �ź��� �Ÿ� Ȯ��
            # �ź����� �Ÿ��� 20�̸��϶�
            t1.turtlesize(3); t2.turtlesize(3); t3.turtlesize(3) # �ź��� ������ ����(3��)
            t1.stamp(); t2.stamp(); t3.stamp();
            t1.turtlesize(1); t2.turtlesize(1); t3.turtlesize(1)
        if (swidth/2 < t1X or t1X < -swidth/2) or (swidth/2 < t2X or t2X < -swidth/2) or (swidth/2 < t3X or t3X < -swidth/2) or \
           (sheight/2 < t1Y or t1Y < -sheight/2) or (sheight/2 < t1Y or t2Y < -sheight/2) or (sheight/2 < t1Y or t3Y < -sheight/2):
            t1.goto(-100, -100); t2.goto(0, 0); t3.goto(100, 100)
            
##            break # while�� Ż��
        
turtle.done()
