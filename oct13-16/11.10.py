import sys
def rotate(x,n):
 b = []
 e = []
 for f in open(x):
  d = dict()
  key = 1
  for c in f:
   d[c] = key
   key = key+1
   b.append(d)
   if b == b[n:]+b[:n]:
    print b
n = int(input())
rotate('word.txt',n)
if __name__ == "__rotate__":
 rotate(x)
