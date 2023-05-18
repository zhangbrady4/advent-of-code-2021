import re
import math

f = open('input.txt', 'r')
g = re.split(",",f.read())

a={}
sum=0
temp=0
big=[]
s=0
t=0

for x in range(len(g)):
    g[x]=int(g[x])
    if g[x] > temp:
        temp=g[x]

#print(g)
print(temp)

for x in range(0,temp+1):
    d=0
    for y in range(len(g)):
        k1=min(x,g[y])
        k2=max(x,g[y])
        tot=k2-k1
        if tot!=0:
            d+=((tot+1)*tot/2)
    big.append(d)

'''for x in range(len(g)):
    d=0
    k1=min(s,g[x])
    k2=max(s,g[x])
    diff=k2-k1
    for y in range(1,diff+1):
        d+=y
    t+=d

print(t)'''

#print(big)

print(min(big))

f.close()
