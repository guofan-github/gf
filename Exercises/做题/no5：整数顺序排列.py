"""
Python整数顺序排列，编程练习题实例五
整数顺序排列问题简述：任意三个整数类型，x、y、z

提问：要求把这三个数，按照由小到大的顺序输出 Python解题思路分析：

首先，要想方法把最小的数放到x位上，之后将x与y进行比较；
如果x>y的话，就将x与y的值进行交换； 然后再用x与z进行比较，
如果x>z则将x与z的值进行交换，这样能使x最小。
"""
# # 使用列表的sort排序
# x = int(input('请输入x:'))
# y = int(input('请输入y:'))
# z = int(input('请输入z:'))
#
# list = [x,y,z]
# list.sort()
# print(list)


x = int(input('请输入x:'))
y = int(input('请输入y:'))
z = int(input('请输入z:'))
list1 = [x, y, z]
for i in range(1,len(list1)):
    for j in range(0,len(list1)-1):
        if list1[j]>list1[i]:
            list1[j],list1[i] = list1[i], list1[j]

print(list1)