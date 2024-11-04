l=list(map(int,input().split()))
print(l)
max=l[0]
min=l[0]
for i in range(len(l)):
    if(max<l[i]):
        max=l[i]
print(max)
l.remove(max)
max=l[0]
for i in range(len(l)):
    if(max<l[i]):
        max=l[i]
print(max)