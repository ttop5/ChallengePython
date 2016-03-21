if n == 1:
    print 1
else:
    print 1
    print 1, 1
    a = [1,1]
    for i in range(2,n):
        b = [1]
        for j in range(1,len(a)):
            b.append(a[j-1]+a[j])
        b.append(1)
        print " ".join([str(x) for x in b])
        a = b
