# 用来执行测试用例
import unittest
import os
from UT.TC.test_002 import Test_Baidu
from UT.TC.test_003 import Test_xd
from HTMLTestRunner import HTMLTestRunner
import HTMLTestRunnerCN
import time


# 获取当前磁盘路径进行拼装
Down_PR_URL = os.path.dirname(__file__)
# 测试用例的目录
case_url = os.path.join(Down_PR_URL, "TC")
report_url = os.path.join(Down_PR_URL, "Report")

if __name__ == '__main__':
    #     测试用例执行的入口 执行当前页面所有用例
    # unittest.main()

    # 测试套件-盒子
    # 1）创建一个盒子，用来存放对应的测试用例
    suit = unittest.TestSuite()
    # 2)添加测试用例
    # a)添加一个测试用例 需要导包
    # suit.addTest(Test_Baidu('test002'))
    # b)添加多个测试用例 - 导包、列表格式
    # test_list = [Test_Baidu('test002'), Test_Baidu('test003')]
    # suit.addTests(test_list)
    # c)添加某个测试用例中的所有测试用例
    # c-1)load去加载用例
    load = unittest.TestLoader()

    # c-2)再通过addTest()或者addTests方法加用例
    # suit.addTest()-单个
    # suit.addTest(load.loadTestsFromTestCase(Test_Baidu))
    # suit.addTests()-多个
    # testcase_list = [load.loadTestsFromTestCase(Test_Baidu), load.loadTestsFromTestCase(Test_xd)]
    # suit.addTests(testcase_list)

    # d)某个文件夹中的所有内容
    # case_url = r"E:\python-learning\UT"
    suit = unittest.defaultTestLoader.discover(start_dir=case_url, pattern='Test_log.py')

    # 生成报告 以下3） 4） 二选一
    # 3)要创建一个TestRunner执行用例--在控制台打印结果
    # run = unittest.TextTestRunner(verbosity=2)
    # run.run(suit)

    # 4)生成测试报告  --html报告当中
    # 4-1） 下载对应报告模板，放到指定目录python安装目录的lib目录下
    # 4-2） 导入对应包 from HTMLTestRunner import HTMLTestRunner
    # 4-3） 执行测试用例到html报告中
    # report 日期.html
    downdate = time.strftime("%Y-%m-%d", time.localtime())
    name = "report{}.html".format(downdate)
    # report_name = report_url+"//report_02.html"
    report_name = os.path.join(report_url, name)
    with open(report_name, 'wb') as f:
        # run = HTMLTestRunner(stream=f, title="自动化测试报告", description="这是一份测试报告")
        run = HTMLTestRunnerCN.HTMLTestRunner(stream=f, title="自动化测试报告", description="这是一份测试报告", tester="刘美丽")
        run.run(suit)


























