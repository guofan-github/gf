"""
简述：话说有一对可爱的兔子，出生后的第三个月开始，每一月都会生一对小兔子。
当小兔子长到第三个月后，也会每个月再生一对小小兔子.

问题：假设条件，兔子都不死的情况下，问每个月的兔子总数为多少？
2 2 2 4 6 10 16
Python解题思路分析：兔子的规律为数列1,1,2,3,5,8,13,21....，好似斐那波契数列的感觉哦
"""

def rabbit(x):
    if x == 1 :
        return 2
    if x == 2 :
        return 2
    rabbit_list = [2,2]
    for i in range(2, x):
        rabbit_list.append(rabbit_list[-1] + rabbit_list[-2])
    return rabbit_list[-1]


print(rabbit(12))


def rabbit_count(months):
    if months == 1 or months == 2:
        return 2
    else:
        return rabbit_count(months - 1) + rabbit_count(months - 2)

# total_months = 12 # 总月数
# rabbit_total = rabbit_count(total_months)
# print("每个月的兔子总数为:", rabbit_total)
print(rabbit_count(12))