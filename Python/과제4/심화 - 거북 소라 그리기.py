#_*_coding=cp949
#_*_coding: euc-kr
##
##���뿹��02 - �ź��̷� ������ ����ϱ�
import turtle # turtle �ҷ�����
import random as ran

## ���� ���� ���� �κ� ##
i, k, tX, tY = [0]*4 # �ݺ���, �ź��̿� ����� ���� ����
swidth, sheight=800,800 # ����� ����� ���� ����

## ���� �ڵ� �κ� ##
if __name__ == "__main__" :
    turtle.title('�ź� ������') # �׷��� â �̸� ����
    turtle.shape('turtle') # �ź��� ��� ��
    turtle.setup(width = swidth + 50, height = sheight + 50) # �׷��� â ũ�� ����(850,500)
    turtle.screensize(swidth, sheight) # �˹����� ũ�� ����(800,450)
    turtle.penup() # ��ø���
    tX, tY = 0, 0  # ��ǥ�� ���� �ʱ�ȭ
    turtle.goto(tX, tY) # �ź��� ���� ��ǥ�� �̵�(-500,250)

    k=5
    turtle.pendown()
    turtle.pensize(5)
    turtle.speed(0)
    for i in range(0, 160): # 1~9����
        r=ran.random()
        g=ran.random()
        b=ran.random()
        turtle.pencolor(r,g,b)
        turtle.forward(k)
        turtle.left(30)
        k=k+1
##        print(i)
        
    turtle.done()
