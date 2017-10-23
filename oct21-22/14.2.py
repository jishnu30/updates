import sys
def sed(p,r,s,d):
 print p,r,s,d
 try:
  f1 = open('a.txt','r')
  f2 = open('b.txt','w')
  for x in f1:
   x = x.replace(p,r)  
   f2 .write(x)
  f1.close()
  f2.close()
 except:
  print "nop"
def main(name):
 pattern = 'orange'
 replace = 'apple'
 source = name 
 dest = name + '.replaced' 
 sed(pattern,replace,source,dest)
if __name__ == "__main__":
 main(*sys.argv)
