l=list(map(int,input().split()))
l=sorted(l)
s=set(l)
for i in s:
    c=0
    for j in l:
        if i==j:
            c=c+1
    print(i,'_',c)