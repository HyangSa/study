import time
import random

MT=[[1,0,0,0,0,0,0,0,0,0,0,1] for i in range(21)]
MT[20]=[1,1,1,1,1,1,1,1,1,1,1,1]
PT=[[0,0,0,0] for i in range(4)]
NT=[[0,0,0,0] for i in range(4)]
count=0

Z=[[2,2,0],   [0,2,2]]
S=[[0,2,2],   [2,2,0]]
L=[[2,0,0],   [2,2,2]]
J=[[0,0,2],   [2,2,2]]
T=[[0,2,0],   [2,2,2]]
M=[[0,2,2],   [0,2,2]]
I=[[0,2],[0,2],[0,2],[0,2]]
r=0
x_pos=0  # 현재 블럭 x좌표
y_pos=0  # 현재 블럭 y좌표
ny_pos=0 # 다음 블럭 y좌표
inypos=0 

def change(x,lst):
    for i in range(4):
        for j in range(4):
##            print(i,j)
            if i<len(x) and j<len(x[0]):
                lst[i][j]=x[i][j]
            else :
                lst[i][j]=0

                
def nextblock(lst):
    global r,ny_pos
    r=random.randrange(0,7)
    if r==0:
        change(Z,lst)
        ny_pos=1
    elif r==1:
        change(S,lst)
        ny_pos=1
    elif r==2:
        change(L,lst)
        ny_pos=1
    elif r==3:
        change(J,lst)
        ny_pos=1
    elif r==4:
        change(T,lst)
        ny_pos=1
    elif r==5:
        change(M,lst)
        ny_pos=1
    elif r==6:
        change(I,lst)
        ny_pos=3
##    [print(NT[i]) for i in range(-1,-5,-1)]
##    print()
        
def gameover(inypos):
    if r==0 or r==5:
        if MT[inypos][5]==1 or MT[inypos][6]==1: return 1;
    elif r==1:
        if MT[inypos][4]==1 or MT[inypos][5]==1: return 1;
    elif r==2 or r==3 or r==4:
        if MT[inypos][4]==1 or MT[inypos][5]==1 or MT[0][6]==1: return 1;
    elif r==6:
        if MT[inypos][5]==1: return 1;

def findy():
    for i in range(15,-1,-1):
        if PT[i//4][i%4] == 2: return i//4
        
def blockin():
    global inypos
    startline=0
    inypos=0
    count=findy()
    while count>=0:
        if gameover(inypos)==1: return 1
        
        
        MT[startline][4:8]=PT[count]
        
        [print(PT[i],"|",NT[i]) for i in range(0,4)]
        print()
        [print(MT[i]) for i in range(21)]
        print()
        time.sleep(0.5)
        if gameover(inypos)==1: return 1
        if count>=1:
            inypos=inypos+1
            print(count,inypos)
            drop()
        count=count-1
        
    
def drop():
    for i in range(len(MT)-1,-1,-1):
        for j in range(len(MT[0])-1,-1,-1):
            if MT[i][j]==2:
                if MT[i+1][j]!=1 or MT[i-1][j]!=2:
                    MT[i+1][j]=MT[i][j]
                    MT[i][j]=0
def pos():
    global x_pos,y_pos
    y_pos+=1
    x_pos=[i for i, x in enumerate(MT[y_pos]) if x==2]
    print(x_pos, y_pos)
    [print(PT[i],"|",NT[i]) for i in range(0,4)]
    print()
    [print(MT[i]) for i in range(21)]
    print()
    time.sleep(0.5)
    
def dropdisplay():
    global x_pos,y_pos
    x_pos=[i for i, x in enumerate(MT[y_pos]) if x==2]
    if len(x_pos)==1:
        while MT[y_pos+1][x_pos[0]]!=1:
            drop()
            pos()
    elif len(x_pos)==2:
        while MT[y_pos+1][x_pos[0]]!=1 and MT[y_pos+1][x_pos[1]]!=1:
            drop()
            pos()
    elif len(x_pos)==3:
        while MT[y_pos+1][x_pos[0]]!=1 and MT[y_pos+1][x_pos[1]]!=1 and\
              MT[y_pos+1][x_pos[2]]!=1:
            drop()
            pos()
    elif len(x_pos)==4:
        while MT[y_pos+1][x_pos[0]]!=1 and MT[y_pos+1][x_pos[1]]!=1 and\
              MT[y_pos+1][x_pos[2]]!=1 and MT[y_pos+1][x_pos[3]]!=1:
            drop()
            pos()

def blockdrop():
    global x_pos,y_pos
    
    dropdisplay()
    
    for i in range(len(MT)-1,-1,-1):
        for j in range(len(MT[0])-1,-1,-1):
            if MT[i][j]==2:
                MT[i][j]=1
    copys()

    
def copys():
    global y_pos,ny_pos
    for i in range(4):
        for j in range(4):
            PT[i][j]=NT[i][j]
    y_pos=ny_pos
    
if __name__ == '__main__':
    global r,inypos,ny_pos,y_pos
    nextblock(PT)
    y_pos=ny_pos
    while(1):
        nextblock(NT)
        if blockin()==1: break
        blockdrop()
        
