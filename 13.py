# 思路一：循环对2取余统计1的个数，注意边界while a>0

def count(a):
    countof1 = 0
    while a:
        countof1 += a%2
        a=a/2
    return countof1

print count(a)


# 思路二：使用python内置函数bin和count以及切片处理

print (bin(a)[2:]).count('1')
