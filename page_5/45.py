# 可以用用reduce这个内建函数

# 计算出每种砝码能提供的重量
L = []
for i in range(len(w)):
    L.append([])
    for j in range(n[i]+1):
        L[i].append(w[i]*j)
        
# 每种砝码提供一个重量一一列出结果并去重的方法       
def sum(a,b):
    y = []
    for i in a:
        for j in b:
            c = i + j
            if c not in y:
                y.append(c)
    return y

# 使用一元二次操作函数列出总的方案，输出方案数    
L = reduce(sum,L)
print len(L)
