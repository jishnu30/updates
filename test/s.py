import math
import sys
def my_sine(x):
 m = 0
 k = 80
 for i in range(k):
  n = math.factorial(2*i+1)
  f = x**(2*i+1)
  if i % 2 == 0:  
   m += f/n
  else:
   m -= f/n
 print m
a = my_sine(1.2)
   
