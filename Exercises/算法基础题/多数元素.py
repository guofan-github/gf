'''
给定一个大小为 n 的数组，找到其中的多数元素。
多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
'''

# 利用列表的count 统计每个元素的次数，找出大于n/2的那个
# def Majority(array):
#     list_len = int(len(array))
#     many_element = []
#     for i in array:
#         count_element = int(array.count(i))
#         if count_element > list_len / 2 and i not in many_element:
#             many_element.append(i)
#     return many_element[0]

# 利用sorted
def Majority(array):
    nums = sorted(array)
    return nums[len(nums)//2]


print(Majority([555, 555, 555, 555, 2, 66]))
