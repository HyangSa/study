#_*_coding=cp949
#_*_coding: euc-kr
##������
##�ź��̷� 2���� ���� ǥ���ϱ�
import turtle # turtle �ҷ�����

## ���� ���� ���� �κ� ##
num=0 #������ ���� ����
swidth, sheight = 1000, 300 # ����� ����� ���� ����
curX, curY = 0, 0 # ��ǥ�� ����� ���� ����

## ���� �ڵ� �κ� ##
if __name__=='__main__':
    turtle.title('�ź��̷� 2���� ǥ���ϱ�') # �׷��� â �̸� ����
    turtle.shape('turtle') # ��Ʋ ��� ����
    turtle.setup(width = swidth + 50, height = sheight + 50) # �׷��� â ũ�� ����(1050x350)
    turtle.screensize(swidth, sheight) # �˹����� ũ�� ����(1000x300)
    turtle.penup() # �� �ø���
    turtle.left(90) # �ݽð���� 90�� ȸ��

    num = int(input("���ڸ� �Է��ϼ��� : ")) # ���� �Է�
    binary = bin(num) # binary�� �Է¹��� ������ �������� ��ȯ�Ͽ� ����
    curX = swidth / 2 # �˹��� ũ���� �ݸ�ŭ curX�� ����(curX=500)
    curY = 0 # y��ǥ�� ����� �� ����
    for i in range(len(binary)-2): #������ ���� ��ŭ ���� (-2 = 0b ���� �Ұ�)
        turtle.goto(curX,curY)  #�ź��� ��ǥ�̵� �ʱⰪ=(500,0)
        if num & 1 :            # ��Ʈ ���� : (�Էµ� ���� 2����) & 0001 --> (�� ���� 1�̶��)
            turtle.color('red')     # ������ ����������
            turtle.turtlesize(2)    # �ź��� ũ�⸦ 2�� ����
        else :                  # (�Էµ� ���� ������ �� ���� 1�� �ƴ϶��)
            turtle.color('blue')    # ������ �Ķ�������
            turtle.turtlesize(1)    # �ź��� ũ�⸦ 1�� ����
        turtle.stamp()              # Ŀ����� ���� ���
        curX -= 50  # curX = curX - 50 (�ź��� x��ǥ -50)
        num >>= 1   # num = num >> 1 (����Ʈ���� �ѹ�)
 
turtle.done()
            
