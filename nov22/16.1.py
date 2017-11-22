import sys
def print_time(t):
 print '%.2d:%.2d:%.2d' % (t.hour,t.minute,t.second)
class time(object):
 "time"
time=time()
time.hour=8
time.minute=29
time.second=15
print_time(time)
if __name__ == "__print_time__":
 print_time(time)
