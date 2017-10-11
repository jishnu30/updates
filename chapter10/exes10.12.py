import sys
def rev(x):
 b = ''
 d = []
 h = 1
 for f in x:
  b = f
  for w in  x[h:]:
   c = list(w)
   g = ''.join(c)
   c.reverse()
   e = ''.join(c)
   if b == e:
    d.append((str(b)+','+str(g)))
  h = h + 1
 print d
n = int(input("enter the no of strings"))
print "enter the strings"
a = [0 for i in range(n)]
for i in range(n):
 a[i] = raw_input()
rev(a)
if __name__ == "__rev__":
 rev(a)
