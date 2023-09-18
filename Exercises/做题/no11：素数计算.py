"""
Python素数计算输出，编程练习题实例十二
简述：区间范围101-200

要求：判断这个区间内有多少个素数，并逐一输出。

Python解题思路分析：首先，判断这个数是否是素数，
方法：用一个数分别去除2到sqrt(这个数)； 其结果，能被整除，则表明此数不是素数，反之是素数。
"""


def is_sushu(num):
    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True


sushu_list = []
for num in range(101, 201):
    if is_sushu(num):
        sushu_list.append(num)

print('101-200中素数共有：', len(sushu_list), '个')
print('它们是：', sushu_list)
