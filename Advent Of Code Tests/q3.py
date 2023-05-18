d = int(input())
r=[]
f=[]
for x in range(d):
    v=int(input())
    if v in r:
        f[r.index(v)]+=1
    else:
        r.append(v)
        f.append(1)

ma=max(f)
mal=[]

for y in range(len(f)):
    if (f[y]==ma):
        mal.append(y)


maxd=0

if (len(mal)>=2):
    for a in mal:
        for b in mal:
            val=abs(r[a]-r[b])
            if val>maxd:
                maxd=val
else:
    fl=f
    del(fl[mal[0]])
    ma1=r[mal[0]]
    del(r[mal[0]])
    mal2=[]
    max2=max(fl)
    for y in range(len(fl)):
        if (fl[y]==max2):
            mal2.append(y)
    for j in mal2:
        val=abs(ma1-r[j])
        if val>maxd:
            maxd=val


print(maxd)