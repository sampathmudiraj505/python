l=list(map(int,input().split()))
l=sorted(l)
a=[]
for i in l:
    if i not in a:
        a.append(i)
print(a)