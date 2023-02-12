import unittest
import time
import os
from common.HTMLTestRunner import HTMLTestRunner

# 测试报告的存放路径


report_path = "./report/"
# 测试报告的标题
report_title = "ui测试"
# 测试的描述
report_desc = "本次测试是对于智慧水务系统的ui测试"

# 做一个判断，如果有了report目录直接使用，没有则创建
if not os.path.exists(report_path):
    # 没有则创建
    os.mkdir(report_path)

# 构建获取时间日期，作为报告的名字，避免重复
gettime = time.strftime("%Y%m%d%H%M%S")

# 构建测试报告存放路径和名字
filepath = report_path + f"report{gettime}.html"

# 执行测试，生成测试报告

# 执行加载用例的路径
case_path = "./test_case"

# 模糊匹配
suite = unittest.defaultTestLoader.discover(start_dir=case_path, pattern='test_*.py')

with open(filepath, "wb") as f1:
    # 使用HTMLTestRunner
    # 第一个参数指的生成的测试报告给那个文件写入
    # 第一个参数是测试用例的标题
    # 第三个参数是对这一次测试的描述
    runner = HTMLTestRunner(f1, title=report_title, description=report_desc)
    # 执行测试套件
    runner.run(suite)


