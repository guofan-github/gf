"""
Python简单数学计算，编程练习题实例十八
问题描述： 求这样的一组数据和，s=a+aa+aaa+aaaa+aa...a的值，
其中a是一个数字； 例如：2+22+222+2222+22222(此时共有5个数相加)，这里具体是由几个数相加，由键盘控制。
"""

# 根据输入的a的值 和a要计算几次 进行循环+
def math_compute():
    a = int(input('请输入你需要计算的a的值：'))
    times = int(input('请输入你需要计算几个数相加：'))
    s = 0
    for i in range(1, times+1):
        s_part = int(str(a)*i)
        s += s_part
    return s

# 原题给的答案，感觉不如我写的QAQ
# def math_compute():
#     # a = int(input('请输入数字 a：'))
#     # count = int(input('请输入几个数相加：'))
#     res = 0  # 初始化最终求解
#     for i in range(1, count + 1):  # 循环次数与输入的值一样，但从1开始循环
#         t = sum([10 ** j for j in range(i)])  # 计算 10**0 + 10**1 + ... + 10**j
#         res = res + (a * t)  # 再计算 a * t
#     return res


print(math_compute())
