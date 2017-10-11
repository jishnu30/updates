import sys
def histogram(s):
 d = dict()
 for c in s:
  if c in s:
   d[c] = 1
  else:
   d[c] += 1   
 print "histogram",d
c = raw_input("enter the string")
histogram(c)
if __name__ == "__histogram__":
 histogram(s)

 
