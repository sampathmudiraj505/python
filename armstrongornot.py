i = int(input())
a=str(i)
b=len(a)
sum=0
for d in a:
    sum=sum+int(d) ** b
if sum==i:
    print("Armstrong")
else:
    print("Not Armstrong")