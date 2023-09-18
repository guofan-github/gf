"""
题目介绍：
实现一个算法来实现反转字符数组的功能。反转的要求如下：
将字符数组的字符进行反转，例如 ['b', ' ', 'a', 'r'] 变成 ['r', 'a', ' ', 'b']。
将字符数组替换为反转后的数组。
考核点：使用 a,b = b,a 交换变量
"""
# 用截取的方法，支持列表、元组、字符串
def reverse(str_list):
    new_str_list = str_list[::-1]
    return new_str_list

print(reverse(['b', ' ', 'a', 'r']))
print(reverse(['dsafa', '   ', 'a156ds1a6', 'rrrr']))
print(reverse(('11','yy',88)))
print(reverse("ds47a4fa1s6ad"))

# # 答案的算法，无法反转元组和字符串
# def reverse(str_array):
#     if str_array:
#         size = len(str_array)
#         for i in range(size//2):
#             str_array[i], str_array[size-1-i]= \
#                 str_array[size - 1 - i],str_array[i]
#             return str_array
#
# print(reverse(['b', ' ', 'a', 'r']))
# print(reverse(['dsafa', '   ', 'a156ds1a6', 'rrrr']))
