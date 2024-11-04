l=list(map(int,input().split()))
max=l[0]
min=l[0]
for i in range(len(l)):
    if(max<l[i]):
        max=l[i]
print(max)
l.sort()
for i in range(len(l)):
    if(min>l[i]):
        min=l[i]
print(min)