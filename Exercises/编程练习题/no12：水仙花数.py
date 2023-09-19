"""
Python水仙花数for循环应用，编程练习题实例十三
什么是水仙花数？百度一下：水仙花数是指一个 n 位正整数 ( n≥3 )，
它的每个位上的数字的 n 次幂之和等于它本身。（例如：1^3 + 5^3+ 3^3 = 153）。
要求：打印输出所有的"水仙花数"。
Python解题思路分析：
可以利用for循环控制流语句来完成操作。从100-999个数，每个数分解出个位、十位和百位。
"""

# 把100-999打出来呗
flowers_num = []
for n in range(100, 1000):
    str_n = str(n)
    a = int(str_n[0])
    b = int(str_n[1])
    c = int(str_n[2])
    if a ** len(str_n) + b ** len(str_n) + c ** len(str_n) == n:
        flowers_num.append(n)

print(flowers_num)
