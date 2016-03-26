# 暴力大法好

i = 1.000
while i**i < y:
    i += 0.001
m = i**i - y
n = (i-0.001)**(i-0.001) - y
if abs(m)>abs(n):
    x = i-0.001
else:
    x = i
print "%.3f" % x
