n=int(input())
for i in range(0,n+1):
    for s in range(0,n-i):
        print(' ',end='')
    for j in range(1,i+1):
        print(j,end='')
    print()