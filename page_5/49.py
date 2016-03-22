# 使用列表

def get(a,b):
    flag = False
    if a < 0:
        flag = True
        a = -a
    if a == 0:
        return 0
    
    ret = ''
    letter = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    while a != 0:
        n = letter[a%b]
        ret = n + ret
        a = a/b
    
    if flag:
        ret = '-' + ret
    return ret
        

print get(a,b)


# 使用字典（可运行但超时)

d = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

s = ''
flag = True
if a<0:
    a = -a
    flag = False
if a == 0:
    s = 0
else:
    while a != 0:
        n = a%b
        a = a/b
        if n < 10:
            s = str(n) + s
        else:
            s = str(d[n]) + s
if flag == False:
    s = '-' + s
    
print s
