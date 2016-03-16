# 辗转相除法和优雅的交换变量值

if a>b:
    a,b = b,a
while b%a != 0:
    a,b = b%a,a
print a
