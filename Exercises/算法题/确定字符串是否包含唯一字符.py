"""
实现一个算法：识别一个字符串中，是否包含唯一的字符。
如果字符串中的字符都是唯一的，则返回 True，如 '123'。
如果字符串中的字符有重复，则返回 False，如 '1223'。
考核点：集合的用法：set()
"""

def has_unique_chars(string):
    if string is None:
        return False
    return len(set(string)) == len(string)


print(has_unique_chars('ssssbbbbb'))
print(has_unique_chars('sb'))
