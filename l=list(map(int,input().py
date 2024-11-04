l=list(map(int,input().split()))
s=int(input())
for i in s:
    c=0
    for j in l:
        if i==l[j]:
            c+=1
    print(i,'_',c)