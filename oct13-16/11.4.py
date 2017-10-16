import sys
def lookup(s,m):
 for f in s:
  if d[f] == m:
   print f 
n = int(input()) 
a = raw_input()
d = dict()
key = 1
for x in a:
 d[x] = key
 key = key+1
lookup(d,n)
if __name__ == "__lookup__":
 lookup(s,m)

