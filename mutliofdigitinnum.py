n=int(input('Enter the number: '))
b=1
while(n>0):
    c=n%10
    b=b*c
    n//=10
print(b)