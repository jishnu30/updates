import sys
a = raw_input("enter the string")
n = len(a) 
b = ''
for i in range(n): 
 if i >= 0:
  h = a[::-1]
  b = h[i]
  print b
  
