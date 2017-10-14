import sys
def rdfl(x):
 b = []
 for f in open(x):
  b.append(f)
 c = dict(zip (b[::2], b[1::2]))
 print c
rdfl('word.txt')
if __name__ == "__rdfl__":
 rdfl('word.txt')
