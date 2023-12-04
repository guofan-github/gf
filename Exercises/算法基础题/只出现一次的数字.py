'''
给定一个非空的整数数组，该数组中除了一个数字只出现一次以外，剩余的数字都会出现两次，返回只出现一次的数字
'''


# # 利用数组的count，找出总数为1的并返回
# def one_num(array):
#     for i in array:
#         num_count = array.count(i)
#     if num_count==1:
#         return i
#     else:
#         return False

# 将次数为2的存入新列表，次数为1的删了，返回被删的数
def one_num(array):
    twice = []
    for i in array:
        if i not in twice:
            twice.append(i)
        else:
            array.remove(i)
    return array.pop()


print(one_num([2, 2, 44, 44, 55, 55, 99]))
