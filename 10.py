# 最大公约×两个数与最大公约数的积

m = a
n = b
if a > b:
    a,b = b,a
while b%a != 0:
    a,b = b%a,a
print a*(m/a)*(n/a)
