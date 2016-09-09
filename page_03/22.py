# 先切片然后转换成整数再转换成秒相减

a = [ int(i) for i in st.split(':') ]
b = [ int(i) for i in et.split(':') ]
print (a[0]*3600- a[1]*60 -a[2] + b[0]*3600 + b[1]*60 + b[2])


# 使用datetime模块

import datetime

st=datetime.datetime.strptime(st,"%H:%M:%S")
et=datetime.datetime.strptime(et,"%H:%M:%S")
print (et-st).seconds
