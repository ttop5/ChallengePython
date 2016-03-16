# 了解求素数的方法
# oj中要多一行换行才让过

import math
for num in range(2, 101):
    is_prime = True
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            is_prime = False
            break
    if is_prime:
        print num,
print
