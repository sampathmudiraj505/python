n=int(input())
s=n
b=''
while(n>0):
    rem=n%2
    b=str(rem)+b
    n=n//2
print(b[::-1])
s=bin(s)#in-built function for number to binary
print(s[2:])