import math
def distance_points(p1,p2):
  a = p2.x-p1.x
  b = p2.y-p1.y
  distance = math.sqrt(a**2 + b**2)
  print distance
class point(object):
 ""
point1 = point()
point2 = point()
point1.x = 5.0
point1.y = 4.0
point2.x = 8.0
point2.y = 9.0
distance_points(point1,point2)   
