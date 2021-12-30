import math
from sympy import *

x=330.19
realx=-7.53238+(0.05601*x)
print(realx)
# 最底部坐标
# x=229
# xx=499.75081*math.exp(-x/-2393.22057)-193.1132
#
# print(xx)

y=152
realy=-4.8152+(209.78461/(1+((y/32.21135)**1.3252)))
print(realy)


cx=realy
ccc=-359.77681*math.exp(-cx/7.79756)+304.5269
print (ccc)


z=330
if z<405:
    q=15-((405-z)/((405-ccc)/7))
elif z>405:
    q=15+((z-405)/((405-ccc)/7))
else:
    q=405


print(q)

realy=26+(14.5*(39-realy))
realx=15*q+60

print(realx)
print(realy)



# y=Symbol("y")
# print(diff(209.78461/(1+((y/32.21135)**1.3252))),y)


# y=545
# dery=-2.79024039750569*y**0.3252/(0.0100365989406739*y**1.3252 + 1)**2
#


