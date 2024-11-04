x,y=map(int,input().split())
m=min(x,y)
for i in range(1,m+1):
    if(x%i==0 and y%i==0):
        ans=i
print(ans)