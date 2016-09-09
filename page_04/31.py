# 遍历即可

l = len(h)
count = 0
for i in range(1,l-1):
    if h[i-1] < h[i] and h[i] > h[i+1]:
        count += 1
print count
