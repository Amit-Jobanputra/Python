from numpy import *
a1=array([1,2,3,4,5])
a2=a1.view()
a2[3]=40
print(a1)
print(a2)
a1[1]=30
print(a1)
print(a2)

