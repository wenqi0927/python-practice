"""
list 列表
"""

list1 = ["Google","Runoob",1997,2000]
list1[0]=1
list1[1:]=["a","b","c"]
print(list1)
#赋值，返回值[1,"a","b","c"]，赋值只能在索引范围内，上面的列表不能赋值list1[4]

del list1[0]
print(list1)
#删除元素，返回值['a','b','c']


#嵌套列表
a=['a','b','c']
b=[1,2,3]
x=[a,b]
#x返回值为[['a','b','c'],[1,2,3]]
print(len(x),x[0],x[0][1])
#返回值2，['a','b','c']，b
print("========================================")

#取最大/最小值
list2=[1,2,3,4,5]
print(max(list2))
print(min(list2))
#5,1
list3=[[1,2,3],[4,5,6]]
print(max(list3))
print(min(list3))
#[4,5,6]     [1,2,3]
#list4=['a',1,2,3]
#print(max(list4))
#print(min(list4))
#无法读取，str和int


a=[1,2,3,4]
b=[4,5,7,7]
a.append(b)
print(a)
#返回值[1,2,3,4,[4,5,7,7]]

print(b.count(7))
#返回值2，返回7在b中出现的次数

a=[1,2,3,4]
b=[4,5,7,7]
a.extend(b)
print(a)
#返回值[1,2,3,4,4,5,7,7]
print(a.index(4))
#返回值3，返回4在a中第一次出现的索引值
m=[1,2,3]
m.insert(1,8)
print(m)
#返回值[1,8,2,3],insert[1,8]是将8插入索引是1的位置
print(m.pop())
#返回值3，pop()是删除列表最后一个元素并返回删除的值
n=[1,2,8,9,8]
n.remove(8)
print(n)
#返回值[1,2,9,8]，remove() 函数用于移除列表中某个值的第一个匹配项
m.reverse()
print(m)
#返回值[2,8,1]，reverse反向列表中元素
aList = ['xyz', 'zara', 'abc', 'xyz','mnopq']
aList.sort()
print(aList)
aList.sort(key=len)
print(aList)
#排序
a=[1,2,3,4,4]
print(a.clear())
#返回值None
a=[1,2,3,4,5]
print(a.copy())
b=a.copy()
print(b)
