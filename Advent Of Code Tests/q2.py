days = int(input())
n1=list(map(int,input().split()))
n2=list(map(int,input().split()))
s1=[0 for i in range(days+1)]
s2=[0 for i in range(days+1)]

for x in range(days):
    s1[x+1]=s1[x]+n1[x]
for x in range(days):
    s2[x+1]=s2[x]+n2[x]

max=0
for x in range(days+1):
    if (s1[x]==s2[x]):
        max=x

print(max)