# 数学问题：二次方程

flag = 0
for x in range(-2000,2000):
    if x*a == x**2 + b:
        flag = 1
        break
if flag == 1:
    print 'Yes'
else:
    print 'No'
