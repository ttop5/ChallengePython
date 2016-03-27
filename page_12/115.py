# python时间库的应用

# 方法正确但是由于时间库的bug原因，oj数据不能通过

import datetime


day = datetime.datetime.strptime(s, '%Y-%m-%d')
print str(int(day.strftime('%j'))) + " " + str(int(day.strftime('%U')) + 1)


# 增加校验(一脸懵逼)

import time


t = time.strptime(s, '%Y-%m-%d')
if int(time.strftime('%U', time.strptime(s[:5] + '01-01', '%Y-%m-%d'))) == 0:
    print int(time.strftime('%j', t)), int(time.strftime('%U', t)) + 1
else:
    print int(time.strftime('%j', t)), int(time.strftime('%U', t))
