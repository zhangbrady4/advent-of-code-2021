import re
import math

f = open('input.txt', 'r')
g = re.split("\n",f.read())

'''for x in range(len(g)):
    g[x]=int(g[x])'''

#print(g)
count=0
a={}

def num(s):
    if (len(s)==2):
        return 1
    elif (len(s)==3):
        return 7
    elif (len(s)==4):
        return 4
    elif (len(s)==7):
        return 8
    elif (len(s)==5):
        if (tr in s and bl in s):
            return 2
        elif (tr in s and br in s):
            return 3
        else:
            return 5
    elif (len(s)==6):
        if (mid not in s):
            return 0
        elif (tr not in s):
            return 6
        else:
            return 9   

for x in range(len(g)):
    i=g[x].split(" | ")
    j=i[0].split(" ")
    #print(j)
    for y in range(len(j)):
        if (len(j[y])==2):
            a[1]=j[y]
        elif (len(j[y])==3):
            a[7]=j[y]
        elif (len(j[y])==4):
            a[4]=j[y]
        elif (len(j[y])==7):
            a[8]=j[y]
    for z in range(3):
        if (a[7][z] not in a[1]):
            top=a[7][z]
    s1=""
    for b in range(4):
        if a[4][b] not in a[1]:
            s1+=a[4][b]
    #print(s1)
    temp=0
    for c in range(2):
        for d in range(len(j)):
            if len(j[d])==5:
                if s1[c] not in j[d]:
                    break
                else:
                    temp+=1
                if (temp==3):
                    mid=s1[c]
    '''print("top: "+top)
    print("mid: "+mid)'''
    for k in range(2):
        if (mid!=s1[k]):
            tl=s1[k]
            #print("tl: "+tl)
    s2=""
    for d in range(len(j)):
        if len(j[d])==5:
            if tl in j[d]:
                for b in range(len(j[d])):
                    if (j[d][b]!= top and j[d][b]!=mid and j[d][b]!=tl):
                        s2+=j[d][b]
    #print(s2)
    bot=""
    br=""
    temp=0
    for c in range(2):
        for d in range(len(j)):
            if len(j[d])==5:
                if s2[c] not in j[d]:
                    break
                else:
                    temp+=1
                if (temp==3):
                    bot=s2[c]
                    br=s2[1-c]

    '''print("bot: "+bot)
    print("br: "+br)'''
    tr=""
    for c in range(2):
        if (a[1][c]!=br):
            tr=a[1][c]
    #print("tr: "+tr)

    for d in range(len(j)):
        if len(j[d])==7:
            for x in range(len(j[d])):
                if (j[d][x]!=top and j[d][x]!=mid and j[d][x]!=tl and j[d][x]!=bot and j[d][x]!=br and j[d][x]!=tr):
                    bl=j[d][x]
                    #print("bl: "+bl)

    h=i[1].split(" ")
    n=""
    for z in h:
        n+=str(num(z))
    print(n)
    count+=int(n) 

    '''h=i[1].split(" ")
    print(h)
    for z in h:
        if (len(z)==2 or len(z)==3 or len(z)==4 or len(z)==7):
            count+=1'''

print(count)

f.close()
