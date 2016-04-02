# 字典

dic_num = {"0":"零","1": "壹", "2": "贰", "3": "叁", "4": "肆", "5": "伍", "6": "陆", "7": "柒", "8": "捌", "9": "玖"} 
dic_unit = {"0": "","1": "拾", "2": "佰", "3": "仟", "4": "万", "5": "拾", "6": "佰", "7": "仟"}
 
s = "" 
if a < 0:
    s += "负"
    a = -a
 
if a==0:
    s += "零"
 
numList = list(str(a)) 
 
index = len(str(a))-1
wan = 4
#print index
 
for i in range(index+1):
#    print i
    if index-i == 4 and numList[i]=="0" : s += dic_unit[str(index-i)]
    elif index == i and numList[i]=="0" : s += dic_unit[str(index-i)]
    elif numList[i]=="0" and numList[i+1]=="0" : pass
    elif numList[i]=="0": s += dic_num[numList[i]]
    else: s += dic_num[numList[i]] + dic_unit[str(index-i)]
s += "圆"
print s
