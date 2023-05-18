    import re
import math

f = open('input.txt', 'r')
#g = re.split("\n",f.read())
g=f.read()

b=[]
fled=[]
ct=0

for x in g:
    if x!="\n":
        b.append(int(x))

s=(int(math.sqrt(len(b))))
l=len(b)

def flash(idx):
    global ct
    if (b[idx]!= 0 or idx not in fled):
        b[idx]+=1
    if (b[idx]>9):
        if idx not in fled:
            fled.append(idx)
            ct+=1
            if (idx/s>=1): #not top
                flash(idx-s)
            if (idx/s<(l/s-1)): #not bot
                flash(idx+s)
            if (idx%s!=0): #not left
                flash(idx-1)
            if (idx%s!=(s-1)): #not right
                flash(idx+1)
            if (idx/s>=1 and idx%s!=0):
                flash(idx-s-1)
            if (idx/s>=1 and idx%s!=(s-1)):
                flash(idx-s+1)
            if (idx/s<(l/s-1) and idx%s!=0):
                flash(idx+s-1)
            if (idx/s<(l/s-1) and idx%s!=(s-1)):
                flash(idx+s+1)
        b[idx]=0

for x in range(1000):
    fled=[]
    for y in range(len(b)):
        flash(y)
    if len(fled)==100:
        print(x)
        break
    #print(b)

#print(ct)

f.close()
