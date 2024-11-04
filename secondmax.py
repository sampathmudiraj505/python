l=list(map(int,input().split()))
max=0
secondmax=max
for i in range(len(l)):
    if l[i]>max:
        secondmax=max
        max=l[i]
print(secondmax)