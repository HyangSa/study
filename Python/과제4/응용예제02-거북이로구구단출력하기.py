#_*_coding=cp949
#_*_coding: euc-kr
##
##���뿹��02 - �ź��̷� ������ ����ϱ�
import turtle # turtle �ҷ�����

## ���� ���� ���� �κ� ##
i, k, tX, tY = [0]*4 # �ݺ���, �ź��̿� ����� ���� ����
swidth, sheight=800,450 # ����� ����� ���� ����

## ���� �ڵ� �κ� ##
if __name__ == "__main__" :
    turtle.title('�ź� ������') # �׷��� â �̸� ����
    turtle.shape('turtle') # �ź��� ��� ����
    turtle.setup(width = swidth + 50, height = sheight + 50) # �׷��� â ũ�� ����(850,500)
    turtle.screensize(swidth, sheight) # �˹����� ũ�� ����(800,450)
    turtle.penup() # ��ø���
    tX, tY = -500, 250  # ��ǥ�� ���� �ʱ�ȭ
    turtle.goto(tX, tY) # �ź��� ���� ��ǥ�� �̵�(-500,250)

    for i in range(1, 10): # 1~9����
        for k in range(2, 10): # 2~9����
            turtle.goto(tX + 80 * k, tY - 40 * i) # �ݺ��ɶ����� ��ǥ �̵�(x��ǥ ����,y��ǥ ����)
            gugu = str(k) + ' x ' + str(i) + ' = ' + str(k * i) # ����for���� �̿��� ������(k x i = k*i)
            turtle.write(gugu, font=('Arial', 12, 'bold')) # ���ھ���		  
    turtle.done()
