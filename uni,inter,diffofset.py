a=set(map(int,input().split()))
b=set(map(int,input().split()))
print(a.union(b),a,b)#0r print(a|b)
print(a.intersection(b))#or print(a&b)
print(a.difference(b))#or print(a-t)
print(a.symmetric_difference(b))#print(a^t)
print(a.update(b))#adds elements of b to a and duplicate elements are removed
print(a.update(b))
print(a.intersection_update(b))
print(a.difference_update(b))
print(a.symmetric_difference_update(b))