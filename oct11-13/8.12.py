import sys
def rotate(w, n):
  print w[n:] + w[:n]
a = []
a = raw_input("enter the string ")
b = int(input("enter the nmbr "))
rotate(a,b)
if __name__ == "__rotate__":
    print rotate(a,b)

