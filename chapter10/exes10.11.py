import sys
def sorted(d,x):
 s = []
 c = 0
 for f in d:
  if f == x:
   s.append(str(f)+':'+str(c))
  c = c + 1
 print s
n = int(input("enter the number"))
print "enter the number"
a = [0 for i in range(n)]
for i in range(n):
 a[i] = raw_input()
c = raw_input('enter the string')
sorted(a,c)
if __name__ == "__sorted__":
 sorted(a,c)
