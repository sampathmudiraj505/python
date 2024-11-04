n=int(input())
org=n
rev=0
while n!=0:
    rem=n%10
    n=n/10
    rev=rev*10+rem
print(rev)
if rev==org:
   print("palindrome")
else:
    print("Not palindrome")