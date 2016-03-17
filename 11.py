# 既能被2整除又能被5整除的个数

def count(L):
    countof2=countof5=0
    for i in L:
        while i%2 == 0:
            i = i/2
            countof2 += 1
        while i%5 == 0:
            i = i/5
            countof5 += 1
    return min(countof2,countof5)

print count(L)
