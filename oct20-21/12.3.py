import sys
def frequency(s):
 b = []
 i = 1
 for x in s:
  if (x,i) not in b:
   i = 1
  else:
   i += 1 
  b.append((x,i))
 print b
a = raw_input()
frequency(a)
if __name__ == "__frequency__":
 frequency(s)
 
