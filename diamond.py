n=int(input())
for i in range(1,n+1):
    for s in range(1,(n+1)-i):
        print(' ',end=' ')
    for j in range(1,i+i):
        print(j,end=' ')
    print()
for i in range(n-1,0,-1):
    for s in range(1,(n+1)-i):
        print(' ',end=' ')
    for j in range(1,(i+i)):
        print(j,end=' ')
    print()