"""
关于python日期格式的应用练习。用python方法如何输出指定格式形式的日期？

这里你会需要用到import方法导入datetime模块。datatime模块重新封装了time模块，
提供更多接口，提供的类有：date,time,datetime,timedelta,tzinfo
datetime.date(year, month, day) date.max、date.min：
date对象所能表示的最大、最小日期； date.resolution： date对象表示日期的最小单位（天）。
date.today()： 返回一个表示当前本地日期的date对象； date.fromtimestamp(timestamp)：

根据给定的时间戮，返回一个date对象；
"""
import datetime


# 2023-09-20
print(datetime.date.today())

# 20092023
print(datetime.date.today().strftime('%d%m%Y'))

# 创建日期对象:1998-07-28
make_date = datetime.date(1998, 7, 28)

print(make_date.strftime('%Y-%m-%d'))

# 日期计算:加一天
new_date = make_date + datetime.timedelta(days=1)
print(new_date)

# 替换日期
replace_date = make_date.replace(year=make_date.year + 2)
print(replace_date)