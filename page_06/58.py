# 实质还是求两个数的最小公倍数

def LCM(a,b):  # 求最小公倍数的方法
    m = a
    n = b
    if a > b:
        a,b = b,a
    while b%a != 0:
        a,b = b%a,a  # 最后的a为最大公约数
    return a*(m/a)*(n/a)  # 利用最大公约数求除最小公倍数

print reduce(LCM,L)  # 使用reduce方法依次两个两个的求出最小公倍数
