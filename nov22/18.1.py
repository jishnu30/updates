import sys
class Time(object):
 def _init_(self,hour=0,minute=0):
  self.hour = hour
  self.minute = minute
 def _lt_(self,other):
  return (self.hour,self.minute)<(other.hour,other.minute)
 def _gt_(self,other):
  return(self.hour,self.minute)>(other.hour,other.minute)
 def _eq_(self,other):
  return (self.hour,self.minute) == (other.hour,other.minute)
a = Time(hour=8, minute=30)
b = Time(hour=10, minute=30)
print(a<b)
