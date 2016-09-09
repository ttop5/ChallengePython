# 使用try...except...

s="202.115.32.24"

try:
    cs = s.split('.')
    cs = map(int, cs)
    if not len(cs) == 4:
        raise Exception('')
    for i in cs:
        if i<0 or i>255:
            raise Exception('')
except:
    print 'No'
else:
    print 'Yes'
