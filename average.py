n=list(map(int,input().split()))
sum=0
for i in range(len(n)):
    sum=sum+n[i]
print('Average',sum/len(n))