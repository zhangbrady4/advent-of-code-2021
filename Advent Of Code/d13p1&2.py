import re
import math

f = open('0inputd13.txt', 'r')
g = re.split("\n|,",f.read())
#g=f.read()

b=[]
fs={}
#print(g)
l=len(g)
pts={}

for x in range(len(g)):
    l1=l-1-x
    if "fold along y=" in g[l1]:
        ls=[]
        ls.append("y")
        ls.append(int(g[l1][13:]))
        fs[x]=ls
        del g[l1]
    elif "fold along x=" in g[l1]:
        ls=[]
        ls.append("x")
        ls.append(int(g[l1][13:]))
        fs[x]=ls
        del g[l1]

#print(fs)
del g[-1]

for x in range(int(len(g)/2)):
    lis=[]
    lis.append(int(g[x*2]))
    lis.append(int(g[x*2+1]))
    pts[x]=lis

#print(pts)

for x in range(len(fs)):
    p={}
    fv=fs[len(fs)-1-x][1]
    if fs[len(fs)-1-x][0]=="y":
        ke=0
        for y in range(len(pts)):
            ll=[]
            xval=pts.get(y)[0]
            ll.append(xval)
            if pts.get(y)[1]>fv:
                yval=(fv+(fv-pts.get(y)[1]))
            else:
                yval=pts.get(y)[1]
            ll.append(yval)
            if ll not in p.values():
                p[ke]=ll
                ke+=1
    elif fs[len(fs)-1-x][0]=="x":
        ke=0
        for y in range(len(pts)):
            ll=[]
            if pts.get(y)[0]>fv:
                xval=(fv+(fv-pts.get(y)[0]))
            else:
                xval=pts.get(y)[0]
            ll.append(xval)
            yval=pts.get(y)[1]
            ll.append(yval)
            if ll not in p.values():
                p[ke]=ll
                ke+=1
    pts=p
    #print(len(pts))


#print(pts)
#print(len(pts))

xmax=0
ymax=0

for x in range(len(pts)):
    if pts.get(x)[0]>xmax:
        xmax=pts.get(x)[0]

for x in range(len(pts)):
    if pts.get(x)[1]>ymax:
        ymax=pts.get(x)[1]

print(xmax)
print(ymax)

for x in range(ymax+1):
    for y in range(xmax+1):
        ch=[]
        ch.append(y)
        ch.append(x)
        if ch in pts.values():
            print("#",end="")
        else:
            print(" ",end="")
    print()

f.close()
