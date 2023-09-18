"""
Python数学计算，编程练习题实例一：
简述：这里有四个数字，分别是：1、2、3、4

提问：能组成多少个互不相同且无重复数字的三位数？各是多少？

Python解题思路分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
"""


def math():
    num_list = []

    for ge in range(1, 5):

        for shi in range(1, 5):

            for bai in range(1, 5):
                if ge != shi and shi != bai and ge != bai:
                    num = f'{ge}{shi}{bai}'
                    num_list.append(int(num))
                    print(int(num))
    print('能组成互不相同且无重复数字的三位数：', len(num_list), '个')


math()
