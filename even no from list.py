l=[int(i) for i in input().split()]
print(l)
e=[]
for i in range(len(l)):
    if l[i]%2==0:
        e.append(l[i])
print('\n' e)