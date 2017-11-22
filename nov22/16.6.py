import sys
def time_to_int(time):
 minutes = time.hour*60 + time.minute
 seconds = minutes*60 + time.second
 return seconds
def int_to_time(seconds):
 time = Time()
 minutes,time.second = divmod(seconds,60)
 time.hour,time.minute = divmod(minutes,60)
 s = '%.2d:%.2d:%.2d' % (time.hour,time.minute,time.second)
 print s
def mul_time(time,factor):
 seconds = time_to_int(time)
 seconds *= factor
 seconds = int(seconds)
 return int_to_time(seconds)
def average_pace(time,distance):
 return mul_time(time,1/distance)
class Time(object):
 ""
clock = Time()
clock.hour = 3.00
clock.minute = 30.00
clock.second = 00
b = 2
mul_time(clock,b)
