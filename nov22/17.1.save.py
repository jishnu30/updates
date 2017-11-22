import sys
class time(object):
 def time_to_int(sec):
  minute = sec.hour*60 + sec.minute
  seconds = minute*60 + sec.second
  print seconds
clock=time()
clock.hour=10.00
clock.minute=20.00
clock.second=30
clock.time_to_int()

