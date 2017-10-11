import sys
def remove(b):
 c = []
 for x in b:
  if x not in c:
   c.append(x)
 print c
n = int(input("enter the number:"))
print "enter the numbers"
a = [0 for i in range (n)]
for i in range (n):
 a[i] = raw_input()
remove(a)
if __name__ == "__remove__":
 remove(a)

