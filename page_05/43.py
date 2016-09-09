# 注意是输出a

a = b = 1
for i in range(1,n):
    c = (a+b) % 20132013
    a = b
    b = c
print a
