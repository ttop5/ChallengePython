# 数学题

L = []
for i in range(b/a):
    if (b/a)%(i+1) == 0:
        L.append(i+1)
print str(L[len(L)/2-1]*a) + " " + str(L[len(L)/2]*a)
