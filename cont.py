s=input()
s=sorted(s)
l=set(s)
for i in l:
    print(i,'_',s.count(i))