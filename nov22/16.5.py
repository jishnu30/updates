import sys
def add_time(t1,t2):
 t1 = valid_time(t1)
 t2 = valid_time(t2)
 seconds = time_to_int(t1) + time_to_int(t2)
 return int_to_time(seconds)
def valid_time(s):
 if s.hour < 0 or s.minute < 0 or s.second < 0:
  return false
 if s.minute >= 60 or s.second >= 60:
  return false
 return s
def int_to_time(seconds):
 time = Time()
 minutes, time.second = divmod(seconds,60)
 time.hour, time.minute = divmod(minutes,60)
 s = '%.2d:%.2d:%.2d' % (time.hour,time.minute,time.second)
 print s
def time_to_int(time):
 minutes = time.hour*60 + time.minute
 seconds = minutes*60 + time.second
 return seconds
class Time(object):
 ""
start = Time()
start.hour = 10.0
start.minute = 30.0
start.second = 07
duration = Time()
duration.hour = 1.00
duration.minute = 25.00
duration.second = 00
add_time(start,duration)
