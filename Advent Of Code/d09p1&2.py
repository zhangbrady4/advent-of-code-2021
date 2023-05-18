import re
import math

f = open('input.txt', 'r')
#g = re.split("\n",f.read())
g = f.read()

b=[]
c=[]
idx=[]
count=1
ln=1

'''for x in range(len(g)):
    g[x]=int(g[x])'''

for x in range(len(g)):
    if g[x]!="\n":
        b.append(int(g[x]))
    else:
        ln+=1

row=int(len(b)/ln)

def basin(y):
    if (y==0): #0
        if (b[y]<b[y+1] and b[y+1]!=9):
            if y+1 not in idx:
                idx.append(y+1)
            basin(y+1)
        if (b[y]< b[row] and b[row]!=9):
            if row not in idx:
                idx.append(row)
            basin(row)
    elif (y==len(b)-1): #49
        if (b[y]<b[y-1] and b[y-1]!=9):
            if y-1 not in idx:
                idx.append(y-1)
            basin(y-1)
        if (b[y]< b[y-row] and b[y-row]!=9):
            if y-row not in idx:
                idx.append(y-row)
            basin(y-row)
    elif (y==row-1): #9
        if (b[y]<b[y-1] and b[y-1]!=9):
            if y-1 not in idx:
                idx.append(y-1)
            basin(y-1)
        if (b[y]< b[y+row] and b[y+row]!=9):
            if y+row not in idx:
                idx.append(y+row)
            basin(y+row)
    elif (y==len(b)-row): #40
        if (b[y]<b[y+1] and b[y+1]!=9):
            if y+1 not in idx:
                idx.append(y+1)
            basin(y+1)
        if (b[y]< b[y-row] and b[y-row]!=9):
            if y-row not in idx:
                idx.append(y-row)
            basin(y-row)
    elif (y%row==0): #10s
        if (b[y]<b[y+1] and b[y+1]!=9):
            if y+1 not in idx:
                idx.append(y+1)
            basin(y+1)
        if (b[y]< b[y-row] and b[y-row]!=9):
            if y-row not in idx:
                idx.append(y-row)
            basin(y-row)
        if (b[y]< b[y+row] and b[y+row]!=9):
            if y+row not in idx:
                idx.append(y+row)
            basin(y+row)
    elif (y/row<1): #1-8
        if (b[y]<b[y+1] and b[y+1]!=9):
            if y+1 not in idx:
                idx.append(y+1)
            basin(y+1)
        if (b[y]<b[y-1] and b[y-1]!=9):
            if y-1 not in idx:
                idx.append(y-1)
            basin(y-1)
        if (b[y]< b[y+row] and b[y+row]!=9):
            if y+row not in idx:
                idx.append(y+row)
            basin(y+row)
    elif (y%row==row-1): #9s
        if (b[y]< b[y-row] and b[y-row]!=9):
            if y-row not in idx:
                idx.append(y-row)
            basin(y-row)
        if (b[y]<b[y-1] and b[y-1]!=9):
            if y-1 not in idx:
                idx.append(y-1)
            basin(y-1)
        if (b[y]< b[y+row] and b[y+row]!=9):
            if y+row not in idx:
                idx.append(y+row)
            basin(y+row)
    elif (y/row>(ln-1)): #40s
        if (b[y]<b[y+1] and b[y+1]!=9):
            if y+1 not in idx:
                idx.append(y+1)
            basin(y+1)
        if (b[y]<b[y-1] and b[y-1]!=9):
            if y-1 not in idx:
                idx.append(y-1)
            basin(y-1)
        if (b[y]< b[y-row] and b[y-row]!=9):
            if y-row not in idx:
                idx.append(y-row)
            basin(y-row)
    else:
        if (b[y]<b[y+1] and b[y+1]!=9):
            if y+1 not in idx:
                idx.append(y+1)
            basin(y+1)
        if (b[y]<b[y-1] and b[y-1]!=9):
            if y-1 not in idx:
                idx.append(y-1)
            basin(y-1)
        if (b[y]< b[y-row] and b[y-row]!=9):
            if y-row not in idx:
                idx.append(y-row)
            basin(y-row)
        if (b[y]< b[y+row] and b[y+row]!=9):
            if y+row not in idx:
                idx.append(y+row)
            basin(y+row)

for y in range(len(b)):
    if (y==0):
        if (b[y]<b[y+1] and b[y]< b[row]):
            c.append(y)
            #count+=(b[y]+1)
    elif (y==len(b)-1):
        if (b[y]<b[y-1] and b[y]< b[y-row]):
            c.append(y)
            #count+=(b[y]+1)
    elif (y==row-1): #9
        if (b[y]<b[y-1] and b[y]< b[y+row]):
            c.append(y)
            #count+=(b[y]+1)
    elif (y==len(b)-row): #40
        if (b[y]<b[y+1] and b[y]< b[y-row]):
            c.append(y)
            #count+=(b[y]+1)
    elif (y%row==0):
        if (b[y]<b[y+1] and b[y]< b[y-row] and b[y]< b[y+row]):
            c.append(y)
            #count+=(b[y]+1)
    elif (y/row<1):
        if (b[y]<b[y+1] and b[y]<b[y-1] and b[y]< b[y+row]):
            c.append(y)
            #count+=(b[y]+1)
    elif (y%row==row-1):
        if (b[y]< b[y+row] and b[y]<b[y-1] and b[y]< b[y-row]):
            c.append(y)
            #count+=(b[y]+1)
    elif (y/row>(ln-1)):
        if (b[y]<b[y+1] and b[y]<b[y-1] and b[y]< b[y-row]):
            c.append(y)
            #count+=(b[y]+1)
    else:
        if (b[y]<b[y+1] and b[y]<b[y-1] and b[y]< b[y-row] and b[y]< b[y+row]):
            c.append(y)
            #count+=(b[y]+1)

a={}
#print(count)
print(c)

d=[]
e=[]


for x in c:
    idx=[]
    o=basin(x)
    d.append(len(idx)+1)
    print(d)

for i in range(0,3):
    max1=0
    for j in range(len(d)):
        if d[j]>max1:
            max1=d[j]

    d.remove(max1)
    e.append(max1)

print(e)

for y in e:
    count*=y

print(count)

f.close()
