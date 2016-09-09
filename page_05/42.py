# 先求出所有的素数再判断

import math


# 求素数放入列表
prime = []
for num in range(2, 10000):
    is_prime = True
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(num)

# 判断
count = 0
for m in prime:
    if n-m in prime:
        count += 1
print count/2  # 去掉重复的情况，再利用四舍五入去掉5,5这种情况（如n=10有：3,7; 5,5; 7,3三种，答案是只有一种）
