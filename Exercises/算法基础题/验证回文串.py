"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。
"""

def check_Palindrome_str(str1):
    #首先把传参都变小写
    str = str1.lower()
    str_list = []
    # 循环从字符串中拿，放进列表，便于计算中间数
    for i in str:
        # 判断是字母数字，放进列表
        if i.isalnum():
            str_list.append(i)
    # 计算中位数（+1 是因为我们从列表取值左闭右开）（//是因为/取的是浮点数且遇到单数会有0.5，//丢弃小数部分）
    middle = len(str_list)//2 +1
    if str_list[:middle] == str_list[:-middle-1:-1]:
        return True
    else:
        return False


print(check_Palindrome_str(' Abc&*^*&^ba '))
print(check_Palindrome_str("A man, a plan, a canal: Panama"))
print(check_Palindrome_str("abccba"))
print(check_Palindrome_str('    '))
print(check_Palindrome_str('啊啊的啊啊'))
print(check_Palindrome_str(''))

