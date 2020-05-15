
def clock(ticks):
##    hours = 0
##    minutes = 0
##    for tick in range(ticks):
##        print('{0:>2}:{1:0>2}'.format(hours, minutes))
##        if minutes == 59:
##            hours += 1
##        minutes = (minutes + 1) % 60

    for m in range(ticks):
        hours = m // 60 # Floor division to round down
        minutes = m % 60
        print('{0:>2}:{1:0>2}'.format(hours, minutes))
        

clock(100)
