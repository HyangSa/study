#_*_coding=cp949
#_*_coding: euc-kr
## �� ������
## [���α׷� 2]�� �ϼ�
import turtle
import random
## ���� ���� ���� �κ� ##
swidth, sheight, pSize, exitCount = 300, 300, 3, 0 #���� 4�� ����
r, g, b, angle, dist, curX, curY = [0]*7 #���� 7�� ����

## ���� �ڵ� �κ� ##
turtle.title('�ź��̰� ����� �ٴϱ�') #�׷��� â �̸� ����
turtle.shape('turtle') # ��Ʋ ��� ����
turtle.pensize(pSize)   #�� �β� ����(3)
turtle.setup(width=swidth+30,height=sheight+30) #�׷��� â ũ�� ����(330x330)��
turtle.screensize(swidth,sheight) #�˹����� ũ�� ����(300x300)

while True :
    r = random.random() #���� r�� 0~1�� ���� ����
    g = random.random() #���� g�� 0~1�� ���� ����
    b = random.random() #���� b�� 0~1�� ���� ����
    turtle.pencolor((r,g,b)) # ���� r,g,b�� �� ���� ����

    angle = random.randrange(0,360) # angle�� 0~359 ������ ���� ����
    dist = random.randrange(1,100) # dist�� 1~99 ������ ���� ����
    turtle.left(angle)  # �������� angle��ŭ ȸ��
    turtle.forward(dist) # dist��ŭ ����
    curX = turtle.xcor() # curX = ���� �ź��� x��ǥ
    curY = turtle.ycor() # curY = ���� �ź��� y��ǥ

    if (-swidth/2<=curX and curX<=swidth/2) and \
       (-sheight/2<=curY and curY<=sheight/2) :
        pass # �ź����� x,y��ǥ�� �˹��� ũ�� �ȿ� ���� ��� if�� ���
    else :   # ���ǽĿ� ���� �ƴ� ���
        turtle.penup()  # �� �ø���
        turtle.goto(0,0)# 0,0 ��ǥ�� �ź��� �̵�
        turtle.pendown()# �� ������

        exitCount += 1 # exitCount 1 ����
        if exitCount >= 5 : # exitCount �� 5�̻��� ��� 
            break # while�� Ż��
turtle.done() #Tkinter�� mainloop �Լ��� ȣ��
