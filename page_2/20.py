# 注意%26即可

letter = 'abcdefghijklmnopqrstuvwxyz'
afterL = ''
for x in a:
    y = (letter.find(x)+b)%26
    afterL += letter[y]
print afterL
