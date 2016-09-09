# 遍历字典

for k,v in t.items():
    if k != 'year' and len(v) ==1:
        t[k] = "0" + t[k]
print("%4s-%2s-%2s %2s:%2s:%2s" %(t["year"],t["month"],t["day"],t["hour"],t["minute"],t["second"]))


# 使用datetime

from datetime import datetime
for k,v in t.items():
    t[k] = int(v)
dt = datetime(t['year'],t['month'],t['day'],t['hour'],t['minute'],t['second'])
print dt.strftime("%Y-%m-%d %X")


# 格式化方法

print ("{:0>4}-{:0>2}-{:0>2} {:0>2}:{:0>2}:{:0>2}" .format(t['year'],t['month'],t['day'],t['hour'],t['minute'],t['second']))
