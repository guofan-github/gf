"""
Python日期计算，编程练习题实例四
简述：要求输入某年某月某日

提问：求判断输入日期是当年中的第几天？
Python解题思路分析： 我们就以3月5日这一天为例。首先把前两个月的加起来，
然后再加上5天即本年的第几天。这里有一种特殊的情况，就是闰月，
遇到这种情况且输入月份大于2时需考虑多加一天。
"""
print('请输入日期：')
date = str(input())
year = int(date.split('年')[0])
month = int(date.split('月')[0].split('年')[1])
day = int(date.split('月')[1].split('日')[0])

month_num = 0
for i in range(1, month):
    if i in [1, 3, 5, 7, 8, 10, 12]:
        i = 31
        month_num = month_num + i
    elif i in [4,6,9,11]:
        i = 30
        month_num = month_num + i
    elif year % 4 == 0 and i ==2:
        i = 29
        month_num = month_num + i
    elif i == 2:
        i = 28
        month_num = month_num + i
day_num = month_num + day
print(day_num)


# year = int(input('year:\n'))
# month = int(input('month:\n'))
# day = int(input('day:\n'))
#
# months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
# if 0 < month <= 12:
#     sum = months[month - 1]
# else:
#  print('data error')
# sum += day
#
# leap = 0 # www.iplaypy.com
#
# if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#     leap = 1
# if (leap == 1) and (month > 2):
#     sum += 1
# print('it is the %dth day.' % sum)