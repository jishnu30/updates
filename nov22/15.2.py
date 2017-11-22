import math
class point(object):
 ""
def move_rect(rect,x,y):
 p = point()
 rect.corner.x += x
 rect.corner.y += y
 return rect.corner.x , rect.corner.y
def main():
 class rectangle(object):
  ""
 box = rectangle()
 box.width = 100.00
 box.height = 200.00
 box.corner = point()
 box.corner.x = 10.0
 box.corner.y = 20.0  
 print move_rect(box,50,100)
if __name__ == "__main__":
 main()
