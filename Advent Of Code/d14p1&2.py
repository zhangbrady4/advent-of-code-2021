import re
import math

f = open('input.txt', 'r')
h=f.readline()
blan=f.readline()
g = re.split("\n| -> ",f.read())
#g=f.read()

b={}
print(h)
h=h[:-1]
#print(g)
chars={}
lets={}

for x in range(int(len(g)/2)):
    b[g[x*2]]=g[x*2+1]

#print(b)

for x in range(len(h)):
    if h[x] not in lets:
        lets[h[x]]=1
    else:
        lets[h[x]]+=1

#print(lets)

for x in range(len(h)):
    if (x!=len(h)-1):
        if h[x:x+2] not in chars:
            chars [h[x:x+2]]=1
        else:
            chars[h[x]]+=1

#print(chars)

for x in range(40):
    c={}
    for y in chars:
        t=chars.get(y)
        #for z in range(chars.get(y)):
        ke=y[0]+b[y]
        if ke in c:
            c[ke]+=t
        else:
            c[ke]=t
        k1=b[y]+y[1]
        if k1 in c:
            c[k1]+=t
        else:
            c[k1]=t
        if b[y] in lets:
            lets[b[y]]+=t
        else:
            lets[b[y]]=t
    
    chars=c
        
    '''
    while (y <len(h)):
        #print(y)
        if h[y:y+2] in b:
            s=""
            s=h[:y+1]+b[h[y:y+2]]+h[y+1:]
        h=s
        y+=2
    #print(h)
    #print(len(h))

for x in range(len(h)):
    if h[x] not in chars:
        chars[h[x]]=1
    else:
        chars[h[x]]+=1'''


mos=0

for x in lets:
    if lets.get(x)>mos:
        mos=lets.get(x)

mi=mos

for x in lets:
    if lets.get(x)<mi:
        mi=lets.get(x)

print(chars)
print(lets)
print(mos-mi)


f.close()
