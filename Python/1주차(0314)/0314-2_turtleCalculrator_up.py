import turtle as t

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

    t.penup()
    count=0;
    num=['1','2','3','+',\
         '4','5','6','-',\
         '7','8','9','*',\
         '0','=','C','/']

    for j in range (160,10-1,-50):
        for i in range (-75,75+1,50):
            t.goto(i,j)
            t.write(num[count],align="center",font=("Arial",20))
            count+=1


result=0;
num="";
num1='';
flag=0;
def printf():
    global num,flag
    reset()
    t.goto(0,250)
    t.write(num,align="center",font=("Arial",20))
    
def printr():
    global num,num1,num2,flag
    reset()
    t.goto(0,250)
    t.write((num+"="+str(eval(num))),align="center",font=("Arial",20))

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
    global result,num,num1,flag
    if (x>=-100 and x<=-50): #1번줄 (1,4,7,0)
        if(y<=200 and y>=150):
            num+='1'
        elif(y<=150 and y>=100):
            num+='4'
        elif(y<=100 and y>=50):
            num+='7'
        elif(y<=50 and y>=0):
            num+='0'
            
    elif (x>=-50 and x<=0): #2번줄 (2,5,8,=)
        if(y<=200 and y>=150):
            num+='2'
        elif(y<=150 and y>=100):
            num+='5'
        elif(y<=100 and y>=50):
            num+='8'
        elif(y<=50 and y>=0):
            reset()
            if(num!=""):
                flag=1
                print("result:",eval(num))
                num1=eval(num)
                printr()
            else:
                print("%%%%  set number  %%%%")
    
    elif (x>=0 and x<=50): #3번줄 (3,6,9,C)
        if(y<=200 and y>=150):
            num+='3'
        elif(y<=150 and y>=100):
            num+='6'
        elif(y<=100 and y>=50):
            num+='9'
        elif(y<=50 and y>=0):
            num=""; flag=0; result=0;
            reset()
            print("reset")
    
    elif (x>=50 and x<=100): #4번줄 (+,-,*,/)
        if(y<=200 and y>=150):
            num+='+';
        elif(y<=150 and y>=100):
            num+='-';
        elif(y<=100 and y>=50):
            num+='*';
        elif(y<=50 and y>=0):
            num+='/';
    if flag==0:
        print(num)
        printf()
    if flag==1:
        num=str(eval(num))
        flag=0

    



t.title('계산기')
t.speed(0)
t.hideturtle()
culdraw()
t.onscreenclick(LClick,1)
