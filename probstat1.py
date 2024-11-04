l=list(map(int,input().split()))
m=l[0]
cnt=1
for i in range(0,len(l)):
    if(m<l[i]):
        m=l[i]
        cnt=cnt+1
print(cnt)