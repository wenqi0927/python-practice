a=[]
b=20
print(a and b)
#返回值为[]
a=10
b=20
print(a and b)
#返回值为20
# a and b,a为true时，a and b返回b的值，a 为false时，a and b返回a的值
#任何非0和非空（null）值为true，0 或者 null为false


a=1
b=3
print(a or b)
#返回值为1
a=[]
b=3
print(a or b)
#返回值为3
# a or b,a为true时，a or b返回a的值，a 为false时，a or b返回b的值a


a=10
print(not a)
#返回值为false
a=[]
print(not a)
#返回值为true