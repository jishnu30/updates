import sys
def duplicate(s):
 for f in s:
  if s[f] != 1:
   print "true"
  else:
   print "false"
a = raw_input()
d = dict()
key = 1
for x in a:
 if x not in d:
  d[x] = key
 else:
  d[x] = key+1
duplicate(d)
if __name__ == "__duplicate__":
 duplicate(s)

