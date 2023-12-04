"""
关于用Python方法辨别数据类型可以用python type()方法，
那么想要查看一串字符中每一项的类型，并逐一输出要怎么来处理呢？下面我们就来做这个示例习题吧。
要求：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
Python解题思路分析： 利用while语句,条件为输入的字符不为'\n'。
"""
import unicodedata


def judement_type():
    str = input('请输入你需要辨别的字符串：')
    nums = 0
    low_letter = 0
    upper_letter = 0
    space = 0
    chinese = 0
    others = 0
    for item in str:
        if item.isdigit():
            nums += 1
        elif item.islower():
            low_letter += 1
        elif item.isupper():
            upper_letter += 1
        elif item.isspace():
            space += 1
        elif 'CJK' in unicodedata.name(item):
            chinese += 1
        else:
            others += 1
    result = f'数字：{nums}个，\n小写字母：{low_letter}个，' \
             f'\n大写字母：{upper_letter}个，\n空格：{space}个，' \
             f'\n汉字：{chinese}个，\n其他：{others}个'
    return result


print(judement_type())
