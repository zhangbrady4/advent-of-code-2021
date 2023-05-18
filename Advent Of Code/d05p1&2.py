import re
import math

f = open('input.txt', 'r')
g = re.split(",| -> |\n",f.read())

#print (g)

a={}

'''for x in range(int(len(g)/4)):
    for y in range(4):
        a.append(0)'''

side = int(math.sqrt(len(a)))

def vents(x):
    b=[]
    for z in x:
        b.append(int(z))

    if (int(b[0])==int(b[2])):
        if (b[1]<b[3]):
            for y in range((b[1]),(b[3]+1)):
                s=str(str(b[0])+","+str(y))
                if s in a:
                    a[s]+=1
                else:
                    a[s]=1
        elif (b[3]<b[1]):
            for y in range((b[3]),(b[1]+1)):
                s=str(str(b[0])+","+str(y))
                if s in a:
                    a[s]+=1
                else:
                    a[s]=1

    elif (int(b[1])==int(b[3])):
        if (b[0]<b[2]):
            for y in range((b[0]),(b[2]+1)):
                s=str(str(y)+","+str(b[1]))
                if s in a:
                    a[s]+=1
                else:
                    a[s]=1
        elif (b[2]<b[0]):
            for y in range((b[2]),(b[0]+1)):
                s=str(str(y)+","+str(b[1]))
                if s in a:
                    a[s]+=1
                else:
                    a[s]=1

    elif ((b[3]-b[1])/(b[2]-b[0])== 1 or -1):
        if (b[1]<b[3]):
            if (b[0]>b[2]):
                for y in range(0,b[3]-b[1]+1):
                    s=str(str(b[0]-y)+","+str(b[1]+y))
                    if s in a:
                        a[s]+=1
                    else:
                        a[s]=1
            elif (b[0]<b[2]):
                for y in range(0,b[3]-b[1]+1):
                    s=str(str(b[0]+y)+","+str(b[1]+y))
                    if s in a:
                        a[s]+=1
                    else:
                        a[s]=1
        elif (b[1]>b[3]):
            if (b[0]>b[2]):
                for y in range(0,b[1]-b[3]+1):
                    s=str(str(b[0]-y)+","+str(b[1]-y))
                    if s in a:
                        a[s]+=1
                    else:
                        a[s]=1
            elif (b[0]<b[2]):
                for y in range(0,b[1]-b[3]+1):
                    s=str(str(b[0]+y)+","+str(b[1]-y))
                    if s in a:
                        a[s]+=1
                    else:
                        a[s]=1


def most(x):
    count=0
    for y in x:
        if (x.get(y)>=2):
            count+=1
    print(count)

for x in range(int(len(g)/4)):
    #print(g[(x*4):(x*4+4)])
    vents(g[(x*4):(x*4+4)])

#print(a)
most(a)

f.close()
