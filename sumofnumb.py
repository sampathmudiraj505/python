n=int(input())
b=0
while(n>0):
    c=n%10
    b=b+c
    n//=10
print(b)