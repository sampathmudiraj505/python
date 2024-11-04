s=int(input())
e=int(input())
for num in range(s,e+1):
    c=0
    for i in range(2,num):
        if(num%i==0):
            c+=1
            break
    if(c==0 and num!=1):
        print(num,end=' ')