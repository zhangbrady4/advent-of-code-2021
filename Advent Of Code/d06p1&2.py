import re
import math

f = open('input.txt', 'r')
g = re.split(",",f.read())

#print (g)
a={}

for x in range(len(g)):
    g[x]=int(g[x])

for x in range(len(g)):
    if (g[x]) in a:
        a[(g[x])]+=1
    else:
        a[(g[x])]=1

six=0

for x in range(256):
    six=0
    for y in range(9):
        if y in a:
            if (y!=0):
                if y-1 in a:
                    a[y-1]+=a.get(y)
                else:
                    a[y-1]=a.get(y)
                a[y]=0
            else:
                six=a.get(0)
                a[y]=0
    if 6 in a:
        a[6]+=six
    else:
        a[6]=six
    if 8 in a:
        a[8]+=six
    else:
        a[8]=six

    '''for y in range(len(g)):
        if (g[y]==0):
            g[y]=6
            g.append(8)
        else:
            g[y]=(g[y]-1)'''

print(a)
sum=0
for x in a:
    sum+=a.get(x)

print(sum)

#print (len(g))

f.close()
