# 类似求最大公约数

count = 0
for x in range(1,min(a,b)+1):
    if a % x == 0 and b % x == 0:
        count += 1
print count
