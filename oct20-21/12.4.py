import sys
def word_list(a):
 b = []
 for x in open(a):
  m = sorted(x)
  for y in open(a):
   r = sorted(y)
   if x != y:
    if m == r: 
     b.append((x,y))
     if  m != r:
      b.remove((x,y))
 print b
word_list('wl.txt')
if __name__ == "__word_list__":
 word_list(a)

