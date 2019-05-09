#_*_coding=cp949
#_*_coding: euc-kr
## 2���� ����Ʈ
## [���α׷� 1]�� �ϼ�
import turtle
import random
##turtle.speed(0)
## ���� ���� ���� �κ� ##
myTurtle, tX, tY, tColor, tSize, tShape = [None]*6 # �ź��� �Ӽ� ���� ����
shapeList = [] # ��� ����Ʈ ����
playerTurtles = [] # �ź��� ����Ʈ ����
swidth,sheight = 500, 500 # ������ ���� ����
## ���� �ڵ� �κ� ##
if __name__=="__main__":
    turtle.title("�ź� ����Ʈ Ȱ��") # �׷��� â �̸� ����
    turtle.setup(width=swidth+50, height = sheight+50) # �׷��� â ũ�� ����
    turtle.screensize(swidth, sheight) # �˹����� ũ�� ����

    shapeList=turtle.getshapes() #�ź��� ��� ����
    for i in range(0,100): # i:0~99���� �ݺ�
        random.shuffle(shapeList) # ������ �ź��� ��� ���� ����
        myTurtle = turtle.Turtle(shapeList[0]) # ���� �ź��� ����� 1��° ������� �ź��� ��� ����
        tX = random.randrange(-swidth/2,swidth/2) # X��ǥ = -250~250 ���� (ĵ���� ������~������ ���� ����)
        tY = random.randrange(-sheight/2,sheight/2) # Y��ǥ = -250~250 ���� (�� �Ʒ����� �� �� ���� ����)
        r=random.random();g=random.random();b=random.random() # r,g,b ���� ����(0~1 ����)
        tSize=random.randrange(1,3) # �ź��� ũ�� ����(1~3)
        playerTurtles.append([myTurtle,tX,tY,tSize,r,g,b]) # �ź��� ����Ʈ�� �ź��� �Ӽ��� ���� ����Ʈ �߰�
        
    for tList in playerTurtles: # ����Ʈ �ϳ��� �ݺ�(ó������ ������)
        myTurtle = tList[0] # ���
        myTurtle.color((tList[4],tList[5],tList[6])) # �ź��� ��
        myTurtle.pencolor((tList[4],tList[5],tList[6])) # �� ��
        myTurtle.turtlesize(tList[3]) # �ź��� ũ��
        myTurtle.goto(tList[1],tList[2]) # �̵� ��ǥ
    turtle.done() # â ����.
#[[<turtle.Turtle object at 0x0000017CE9EE6A58>, -191, 199, 2, 0.5086602159715642, 0.06106201906133513, 0.4823624918923082]
