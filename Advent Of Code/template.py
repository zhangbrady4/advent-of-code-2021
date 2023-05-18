import re
import math

f = open('input.txt', 'r')
#h=f.readline()
#blan=f.readline()
#g = re.split("\n",f.read())
#g = f.read()

print(g)
b=[]

'''for x in range(len(g)):
    g[x]=int(g[x])'''

for x in g:
    if x!="\n":
        b.append(int(x))
    else:
        ln+=1

f.close()
