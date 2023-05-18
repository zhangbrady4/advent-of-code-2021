import re
import math

f = open('input.txt', 'r')
g = re.split("\n|-",f.read())
#g=f.read()

#print(g)
b={}
low=[]
path=[]
count=0

for x in range(int(len(g)/2)):
    a=[]
    if(g[x*2]!="start" and g[x*2]!="end"):
        '''if g[x*2].islower() and g[x*2] not in low:
            low.append(g[x*2])'''
    if(g[x*2+1]!="start" and g[x*2+1]!="end"):
        '''if (g[x*2+1].islower() and g[x*2+1] not in low):
            low.append(g[x*2+1])'''
    a.append(g[x*2])
    a.append(g[x*2+1])
    b[x]=(a)

print(b)

def pats(s,s1,l,f):
    tf=f
    temp=[]
    for x in range(len(l)):
        temp.append(l[x])
    global count
    if (s=="end"):
        count+=1
        return
    if (s.islower()):
        temp.append(s)
        if temp.count(s)>1:
            tf=1
    for x in range(len(b)):
        if b.get(x)[0]==s and b.get(x)[1]!="start":
            if(tf==0):
                if temp.count(b.get(x)[1])<2:
                    pats(b.get(x)[1],s,temp,tf)
            elif b.get(x)[1] not in temp:
                pats(b.get(x)[1],s,temp,tf)
        elif (b.get(x)[1]==s and b.get(x)[0]!="start"):
            if(tf==0):
                if temp.count(b.get(x)[0])<2:
                    pats(b.get(x)[0],s,temp,tf)
            elif b.get(x)[0] not in temp:
                pats(b.get(x)[0],s,temp,tf)

for x in range(len(b)):
    if b.get(x)[0]=="start":
        low=[]
        pats(b.get(x)[1],"start",low,0)
    elif b.get(x)[1]=="start":
        low=[]
        pats(b.get(x)[0],"start",low,0)

print(count)

'''for x in g:
    if x!="\n":
        b.append(int(x))'''

f.close()
