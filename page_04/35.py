# 用m存最大的值，如果累加和大于m，则改变m，一旦s加到负数小于零就置零重算。m始终是最大的序列和

M = max(L)
S = 0
for x in L:
    S += x
    M = max(M,S)
    S = max(S,0)
print M
