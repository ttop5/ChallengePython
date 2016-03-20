# 注意边和角的关系

l = [a,b,c]
l.sort()
if (l[0] + l[1]) <= l[2]:
    print 'W'
elif (l[0]**2 + l[1]**2) == l[2]**2:
    print 'Z'
elif (l[0]**2 + l[1]**2) > l[2]**2:
    print 'R'
else:
    print 'D'
