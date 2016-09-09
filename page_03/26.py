# 分别和升序降序后的列表进行比较

if L == sorted(L):
    print 'UP'
elif L == sorted(L)[::-1]:
    print 'DOWN'
else:
    print 'WRONG'
