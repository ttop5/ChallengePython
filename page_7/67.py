# 根据题意一步步来

s = 8
count = 1
while s > 0:
    m = int(str(M)[::-1])
    sum  = M + m
    if sum != int(str(sum)[::-1]):
        count += 1
        s -= 1
        M = sum
    else:
        break
if s>0:
    print count
else:
    print 0
