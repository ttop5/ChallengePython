# 思路一：双循环逐个比较

flag = 0
for i in range(0,len(L)-2):
    for j in range(i+1,len(L)-1):
        if L[i] == L[j]:
            flag = 1
        else:
            continue
            
if flag == 1:
    print 'YES'
else:
    print 'NO'


# 思路二：排序后比较相邻的

sort()
for i in range(0,len(L)-1):
    if L[i] == L[i+1]:
        flag = 1
        break

if flag == 1:
    print 'YES'
else:
    print 'NO'
