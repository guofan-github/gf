"""
什么是完数？ 完全数，又被称作完美数或完备数，是一些特殊的自然数。
它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
如果一个数恰好等于它的因子之和，则称该数为“完全数”。 以上，是我们的大百度为大家提供的关于完数的解释。
接下来，就来开始我们的练习吧。

要求：用python方法找出1000以内的所有完数，并输出。
"""
# 使用列表推导式,直接找出1000以内的所有完数
perfect_numbers = [i for i in range(1, 1001) if sum(j for j in range(1, i) if i % j == 0) == i]
# print(perfect_numbers)

# 封装列表推导式
def find_perfect_number(num):
    perfect_numbers = [i for i in range(1, num +1) if sum(j for j in range(1, i) if i % j == 0) == i]
    return perfect_numbers


print(find_perfect_number(10000))


# 下面是我的蠢办法
# 定义一个寻找完美数的方法
def divisor_calculation(num):
    divisor_list = []

    for i in range(1, num):
        if num % i == 0:
            divisor_list.append(i)
    if sum(divisor_list) == num:
        return num
# 循环想要的数字，传入方法中，返回列表
def find_perfectnum(num):
    perfect_number = []
    for i in range(1,num+1):
        perfect = divisor_calculation(i)
        if perfect:
            perfect_number.append(perfect)
    return perfect_number
# print(find_perfectnum(1000))
