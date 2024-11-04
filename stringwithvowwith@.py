s=input()
a=''
for i in s:
    if i in 'aeiouAEIOU':
        a=a+'@'
    elif i==' ':
         a=a+'_'
    else:
        a=a+i
print(a)