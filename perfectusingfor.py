n=int(input())
for i in range(1,n//2+1):
    if i**2==n:
        print('It is perfect')
        exit()
    else:
        continue
print('Not perfect')