# 比较因子2和5的个数，2多输出0;，5多输出1

countof2=countof5=0
for i in L:
    while i%2 == 0:
        i = i/2
        countof2 += 1
    while i%5 == 0:
        i = i/5
        countof5 += 1
if countof2 > countof5:
    print 0
else:
    print 1
