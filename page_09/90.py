# itertool.permutations的妙用

import itertools


a = list(set(itertools.permutations(s)))
# print a
b = sorted(a)
# print b
for i in b:
    print ''.join(i)
