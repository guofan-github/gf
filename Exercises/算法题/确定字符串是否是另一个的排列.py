"""
实现一个算法来识别一个字符串 str2 是否是另一个字符串 str1 的排列。排列的解释如下：

如果将 str1 的字符拆分开，重新排列后再拼接起来，能够得到 str2 ，那么就说字符串 str2 是字符串 str1 的排列。
例如：123 是 321 的排列，abc 是 cba 的排列。
如果 str2 字符串是 str1 字符串的排列，则返回 True；反之则返回 False；
考核点：sorted()方法
"""

def is_sort(str1, str2):
    if str1 is None or str2 is None:
        return False
    return sorted(str1)==sorted(str2)

print(is_sort(None,'s'))
print(is_sort('ssbb', 'bbss'))
print(is_sort(['3758','66ff'],['f6f6','3857']))
print(is_sort('dsa14d4as6','saf8as4dsa4'))
print(is_sort('8s9d4f','4s8f9d'))