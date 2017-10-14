import sys
def interlock(x,y):
 c = ''
 c = zip(x,y)
 print ''.join(''.join(s) for s in c)
a = ''
a = raw_input("enter the frst string : ")
b = ''
b = raw_input("enter the scnd string : ")
interlock(a,b)
if __name__ == "__interlock__":
 interlock(a,b)
