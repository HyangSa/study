#_*_coding=cp949
#_*_coding: euc-kr
##��ø if��
##[���α׷� 1]�� �ϼ�

import turtle # turtle �ҷ�����
## ���� ���� ���� �κ� ##
swidth, sheight = 500, 500 # ����� ����� ���� ����
## ���� �ڵ� �κ� ##
turtle.title('�������� ���׸���') # �׷��� â �̸� ����
turtle.shape('turtle') # ��Ʋ ��� ����
turtle.setup(width = swidth + 50, height = sheight + 50) # �׷��� â ũ�� ����(550x550)
turtle.screensize(swidth, sheight)# �˹����� ũ�� ����(500x500)
turtle.penup() # �� �ø���
turtle.goto(0, -sheight / 2) # ������ǥ�� �̵�(0,-250)
turtle.pendown() # �� ������
turtle.speed(0) # �ӵ� ����

for radius in range(1, 250) : # 1~249���� �ݺ� ����(radius 1�� ����)
    if radius % 6 == 0 : # radius/6 �������� 0�϶�
        turtle.pencolor('red') # ����� ����(����)
    elif radius % 5 == 0 : # radius/5 �������� 0�϶�
        turtle.pencolor('orange') # ����� ����(��Ȳ)
    elif radius % 4 == 0 : # radius/4 �������� 0�϶�
        turtle.pencolor('yellow') # ����� ����(���)
    elif radius % 3 == 0 : # radius/3 �������� 0�϶�
        turtle.pencolor('green')  # ����� ����(�ʷ�)
    elif radius % 2 == 0 : # radius/2 �������� 0�϶�
        turtle.pencolor('blue')   # ����� ����(�Ķ�)  
    elif radius % 1 == 0 : # radius/1 �������� 0�϶�
        turtle.pencolor('navyblue') # ����� ����(����)  
    else :  # �� ���϶� 
        turtle.pencolor('purple') # ����� ����(����)  
    turtle.circle(radius) # ���׸���(radius�� ���������� �� ��)
turtle.done()
