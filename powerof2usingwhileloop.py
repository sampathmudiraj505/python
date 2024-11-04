n=int(input())
i=1
while (2**i<(n)):
    i=i+1
if(2**i==n):
    print('Power of 2')
else:
    print('Not Power of 2')