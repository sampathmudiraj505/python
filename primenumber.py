n=int(input())
m=n
a=0
for i in range(2,n):
    if(n%i==0):
        a=a+1
if(a==0):
    print('is Prime')
else:
    print('Not Prime')