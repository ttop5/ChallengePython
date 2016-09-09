# 乘法运算

print '% 8d'%a
print 'x% 7d'%b
c=b
print '-'*8
i=8
while c>0:
    print '% *d'%(i,(c%10)*a)
    c=c/10
    i-=1
if i==7:
    print '*'*20
else:
    print '-'*8
    print '% 8d'%(a*b)
    print '*'*20
