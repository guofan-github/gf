"""
Python斐波那契数列应用，编程练习题实例六
斐波那契数列（Fibonacci sequence），又称黄金分割数列、
因数学家列昂纳多·斐波那契以兔子繁殖为例子而引入，故又称为“兔子数列”，
指的是这样一个数列：1、1、2、3、5、8、13、21、34、
在数学上，斐波纳契数列以如下被以递归的方法定义。
"""
# def fib(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(6))

"""
问题的要求改为：需要输出指定个数的斐波那契数列，要怎么来解决呢？
"""
def fib(n):
    if n ==1:
        return 1
    if n ==2:
        return [1,1]
    fibs = [1, 1]
    for i in range(2,n):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs
print(fib(5))