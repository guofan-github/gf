"""
给定一个整数 num，从 1 到 num 按照下面的规则返回每个数：

如果这个数被 3 整除，返回 'Fizz'。
如果这个数被 5 整除，返回 'Buzz'。
如果这个数能同时被 3 和 5 整除，返回 'FizzBuzz'。
如果这个数既不能被 3 也不能被 5 整除，返回这个数字的字符串格式。
考核点：Python 基础语法中的条件判断
"""
def FBzz():
    num = int(input('请输入一个整数：'))
    if num < 1:
        raise ValueError('不能比1小！')
    l = []
    for i in range(1, num+1):
        if i % 3 == 0 and i % 5 == 0:
            l.append('FizzBuzz')
        elif i % 3 == 0:
            l.append('Fizz')
        elif i % 5 == 0:
            l.append('Buzz')
        else:
            l.append(str(i))

    return l


x = FBzz()
print(x)