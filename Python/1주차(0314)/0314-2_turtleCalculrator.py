import turtle as t
import os

def sq(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(0,4):
        t.forward(50)
        t.rt(90)

def culdraw():
    t.penup()
    t.goto(-100,300)
    t.pendown()
    t.goto(100,300)
    t.goto(100,200)
    t.goto(-100,200)
    t.goto(-100,300)
    
    for j in range(200,0,-50):
        for i in range(-100,51,50):
            sq(i,j)

def numwrite():
    count=0
    t.penup()
    number=["1","2","3","+",
            "4","5","6","-",
            "7","8","9","*",
            "0","=","C","/"]
    for i in range(160,10-1,-50):
        for j in range(-75,75+1,50):
            t.goto(j,i)
            t.write(number[count],align="center",font=("Arial",20))
            count=count+1
    



result=0;
num="";
num1=0;
num2=0;
flag=0;
def printf():
    global num,num1,num2,flag
    t.goto(0,250)
    numbers=(str(num1)+str(flag)+str(num2))
    t.write((numbers+"="+str(result)),align="center",font=("Arial",20))

def reset():
    t.penup()
    t.goto(-100,300)
    t.fillcolor('white')
    t.begin_fill()
    t.pendown()
    t.goto(100,300)
    t.goto(100,200)
    t.goto(-100,200)
    t.goto(-100,300)
    t.end_fill()
    t.penup()

def LClick(x,y):
    global result,num,num1,num2,flag
    if (x>=-100 and x<=-50): #1번줄 (1,4,7,0)
        if(y<=200 and y>=150):
            num+='1'
            print(num)
        elif(y<=150 and y>=100):
            num+='4'
            print(num)
        elif(y<=100 and y>=50):
            num+='7'
            print(num)
        elif(y<=50 and y>=0):
            num+='0'
            print(num)
            
    elif (x>=-50 and x<=0): #2번줄 (2,5,8,=)
        if(y<=200 and y>=150):
            num+='2'
            print(num)
        elif(y<=150 and y>=100):
            num+='5'
            print(num)
        elif(y<=100 and y>=50):
            num+='8'
            print(num)
        elif(y<=50 and y>=0):
            reset()
            if(num1==0 and flag==0):
                print("result:",num)
            elif(flag!=0 and num==""):
                print("%%%%  set number 2  %%%%")
            elif(flag!=0):
                num2=float(num)
                if(flag=='+'):
                    result=num1+num2
                elif(flag=='-'):
                    result=num1-num2
                elif(flag=='*'):
                    result=num1*num2
                elif(flag=='/'):
                    result=num1/num2
                print("result:",result)
                printf()
                num1=0;
                flag=0
    
    elif (x>=0 and x<=50): #3번줄 (3,6,9,C)
        if(y<=200 and y>=150):
            num+='3'
            print(num)
        elif(y<=150 and y>=100):
            num+='6'
            print(num)
        elif(y<=100 and y>=50):
            num+='9'
            print(num)
        elif(y<=50 and y>=0):
            num=""; num1=0; num2=0; flag=0; result=0;
##            t.undo()
            reset()
            print("reset")
    
    elif (x>=50 and x<=100): #4번줄 (+,-,*,/)

        num1=float(num)
        num=''
        if(y<=200 and y>=150):
            flag='+';
        elif(y<=150 and y>=100):
            flag='-';
        elif(y<=100 and y>=50):
            flag='*';
        elif(y<=50 and y>=0):
            flag='/';


    

t.title('계산기')
t.speed(0)
t.hideturtle()
culdraw()
numwrite()
t.onscreenclick(LClick,1)
