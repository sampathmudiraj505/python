n=int(input('Enter your num:'))
m=n
rev=0
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n//=10
print(rev)
if(rev==m):
    print('Is Palindrome')
else:
    print('NOt palindrome')    