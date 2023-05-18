import re
import math

f = open('input.txt', 'r')
g = re.split("\n",f.read())

#print(g)
count=0
cor=[]
tot=[]

for x in range(len(g)):
    n=[]
    for y in range(len(g[x])):
        s=g[x][y]
        if g[x][y] in "([{<":
            n.append(g[x][y])
        else:
            if (s==")"):
                if (n[-1]=="("):
                    del n[-1]
                else:
                    cor.append(x)
                    count+=3
                    break
            if (s=="]"):
                if (n[-1]=="["):
                    del n[-1]
                else:
                    count+=57
                    cor.append(x)
                    break
            if (s=="}"):
                if (n[-1]=="{"):
                    del n[-1]
                else:
                    count+=1197
                    cor.append(x)
                    break
            if (s==">"):
                if (n[-1]=="<"):
                    del n[-1]
                else:
                    count+=25137
                    cor.append(x)
                    break
    

#print(cor)
for x in range(len(cor)):
    del g[cor[len(cor)-1-x]]

for x in range(len(g)):
    n=[]
    for y in range(len(g[x])):
        s=g[x][y]
        if g[x][y] in "([{<":
            n.append(g[x][y])
        else:
            if (s==")"):
                del n[-1]
            if (s=="]"):
                del n[-1]
            if (s=="}"):
                del n[-1]
            if (s==">"):
                del n[-1]
    score=0
    for z in range(len(n)):
        val=(len(n)-1-z)
        score*=5
        if (n[val]=="("):
            score+=1
        if (n[val]=="["):
            score+=2
        if (n[val]=="{"):
            score+=3
        if (n[val]=="<"):
            score+=4

    tot.append(score)

'''for x in range(len(g)):
    g[x]=int(g[x])'''

tot.sort()
print(tot[int((len(tot)-1)/2)])

f.close()
