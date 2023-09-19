"""
Python乘法口诀计算，编程练习题实例八
简述：9*9乘法口诀表。
要求：逐项单位输出。例如1的一行，2的一行，以此类推。
Python解题思路分析： 注意分行与列考虑。这里共有9行和9列。x控制行，y控制列。
"""

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{j}x{i}={i*j}\t', end='')
    print(' ')


