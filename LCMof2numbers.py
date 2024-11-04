x,y=map(int,input().split())
m=max(x,y)
for i in range(m,(x*y)+1):
    if(i%x==0 and i%y==0):
        print(i)
        break