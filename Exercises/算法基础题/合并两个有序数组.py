"""
合并两个有序数组
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]
"""
# 通过内置函数sorted 合并后排序
# def order_array(nums1,m,nums2,n):
#     # if m>0 and n>0:
#     #     nums1_part = nums1[0:m]
#     #     nums2_part = nums2[0:n]
#     #     for i in nums2_part:
#     #         nums1_part.append(i)
#     #
#     # new_nums1 = sorted(nums1_part)
#     # return new_nums1
#     new_nums = nums1[:m] + nums2[:n]
#     sorted_list = sorted(new_nums)
#     nums1[:] = sorted_list
#     return nums1

# 双指针法
def order_array(nums1,m,nums2,n):

    while m > 0 and n > 0:
        if nums1[m-1]>=nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    if m==0:
        for i in range(n):
            nums1[i] = nums2[i]
    return nums1


print(order_array([1, 2, 3, 4,5,6,7,8,9], 5, [2, 5, 6,9,15,88,99], 2))
print(order_array([1,2,3,0,0,0], 3, [2, 5, 6], 3))


