n=int(input())
a=0
b=1
x=[0,1]
for i in range(2,n):
    c=a+b
    x.append(c)
    a=b
    b=c
print(x)
print(c)