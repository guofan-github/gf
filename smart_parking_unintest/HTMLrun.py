
import os
import time
import unittest

from BeautifulReport import BeautifulReport

from common.HTMLTestRunner import HTMLTestRunner

# 存放报告的路径
report_path = r'D:/pycharm/smart_parking_unintest/report/'

# 测试报告的标题
report_title = "郭凡の测试报告"

# 测试的描述
report_desc = "通过unintest框架实现接口和ui自动化测试"

# 做一个判断，如果有report文件夹就直接使用，如果没有就创建
if not os.path.exists(report_path):
    # 没有就创建一个
    os.mkdir(report_path)

# 获取时间戳作为报告名，避免报告重复
gettime = time.strftime('%Y%m%d-%H-%M-%S')

# 构建测试报告存放路径和名字
file_path = report_path + f'report_{gettime}.html'

# 执行测试，生成测试报告

# 执行加载用例的路径
case_path = './test_case'

# 模糊匹配加入suite
suite = unittest.defaultTestLoader.discover(start_dir=case_path, pattern='test_*.py')

# 使用HTMLTestRunner生成测试报告
with open(file_path, 'wb') as f:
    # 使用HTMLTestRunner
    # 第一个参数指的生成的测试报告给哪个文件写入
    # 第二个参数是测试的标题
    # 第三个参数是对测试的描述
    runner = HTMLTestRunner(f, title=report_title, description=report_desc)
    # 执行测试套件
    runner.run(suite)

