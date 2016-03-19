# 写个方法重复调用

def conv(n,m):
    temp = []
    while n != 0:
        temp.append(n % m)
        n = n/m
    return  sum(temp)

print conv(n,16) == conv(n,12) == conv(n,10) and 'Yes' or 'No'
