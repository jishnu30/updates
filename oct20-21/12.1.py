import sys
n = int(input("enter the limit"))
a = [0 for i in range(n)]
for i in range(n):
 a[i] = int(input()) 
b = tuple(a)
print sum(b)

