import math
import copy
class point(object):
 ""
def move_rect(rect,x,y):
 p = point()
 rect.corner.x += x
 rect.corner.y +=y
def mov_rect_copy(rect,x,y):
 new = copy.copy(rect)
 move_rect(new,x,y)
 return new
def main():
 class rectangle(object):
  ""
 box = rectangle()
 box.width = 100.0
 box.height = 200.0
 box.corner = point()
 box.corner.x = 10.0
 box.corner.y = 20.0
 new_box = mov_rect_copy(box,50,100)
 print box.corner.x
 print box.corner.y
if __name__ == "__main__":
 main()

