s=input()
s1=input()
if len(s)!=len(s1):
    print('Not anagram')
else:
    l=set(s)
    l1=set(s1)
    for i in l:
        if s.count(i)!=s1.count(i):
            print('No Anagram')
            break
        
print('Anagram')
            