s=int(input())
e=int(input())
def primeno(n):
    for i in range(2,n):
        if n%i==0:
            return 'no'
        else:
            continue
    print(n,end=' ')
    
for i in range(s,e+1):
      primeno(i)