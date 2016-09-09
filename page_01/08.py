# 先排序，注意奇偶个数以及下标

L.sort()
l=len(L)
if (l%2)==0:
    print (L[l/2-1]+L[l/2])/2.0
else:
    print L[l/2]
