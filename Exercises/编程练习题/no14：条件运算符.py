"""
要求：获取输入的内容，
并利用条件运算符的嵌套方式来完成这道题。
 学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
"""


def score():
    study_score = int(input('请输入学生成绩：'))
    if study_score>=90:
        print('这位同学的评分为A')
    elif 60<=study_score<89:
        print('这位同学的评分为B')
    elif 0<study_score<60:
        print('这位同学的评分为C')
    else:
        print('沃德发！请输入正确的成绩！')


score()
