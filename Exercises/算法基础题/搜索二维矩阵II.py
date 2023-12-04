'''
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。
该矩阵具有以下特性：
每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例：现有矩阵 matrix 如下：
[
 [1,   4,  7, 11, 15],
 [2,   5,  8, 12, 19],
 [3,   6,  9, 16, 22],
[10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。
给定 target = 20，返回 false。
'''
def search_target_value(matrix, target):
    judge_list = []
    for matrix_list in matrix:
        for element in matrix_list:
            if int(element) == target:
                judge_list.append(element)
    if len(judge_list)>0:
        return True
    else:
        return False

m = [
 [1,   4,  7, 11, 15],
 [2,   5,  8, 12, 19],
 [3,   6,  9, 16, 22],
[10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print(search_target_value(m, 17))
