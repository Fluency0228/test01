# coding = utf-8
# Author:Easy
# Date:2023/6/21 12:31

import selenium
import unittest
from ddt import ddt, data, unpack, file_data
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from UT.common.Read_File import ReadFile
from UT.data.case_url import case_url

def get_case():
    # rf = ReadFile(r'E:\python-learning\UT\data\Test_log.xlsx')
    url = case_url.Log_case_url
    rf = ReadFile(url)
    case_data = rf.read_excel()
    return case_data




@ddt
class Test_log(unittest.TestCase):

    def setUp(self) -> None:
        "打开浏览器的操作"
        self.drive = webdriver.Chrome()
        self.drive.get("http://shop-xo.hctestedu.com/index.php?s=/index/user/logininfo.html")
        self.drive.implicitly_wait(5)

    def tearDown(self) -> None:
        "关闭浏览器的操作"
        time.sleep(3)
        self.drive.quit()

    # 多个数据 单个操作
    # @data(("hami", "123456"), ("yulisa", "123456"))
    # @data(["hami", "123456"], ["yulisa", "123456"])
    # 字典格式时key必须=形参
    @data({"user": "hami", "pwd": "123456"}, {"user": "yulisa","pwd": "123456"})
    @unpack
    def _test_log001(self, user, pwd):
        # 账号 密码 登录
        self.drive.find_element(By.NAME, "accounts").send_keys(user)
        self.drive.find_element(By.NAME, "pwd").send_keys(pwd)
        self.drive.find_element(By.XPATH, '//button[text()="登录"]').click()
        time.sleep(2)
    li = [{"user": "hami", "pwd": "123456"}, {"user": "yulisa","pwd": "123456"}]
    # @data({"user": "hami", "pwd": "123456"}, {"user": "yulisa","pwd": "123456"})
    @data(*li)
    @unpack
    def _test_log002(self, **para):
        print(para)
        self.drive.find_element(By.NAME, "accounts").send_keys(para["user"])
        self.drive.find_element(By.NAME, "pwd").send_keys(para["pwd"])
        self.drive.find_element(By.XPATH, '//button[text()="登录"]').click()
        time.sleep(2)
    @file_data(r"E:\python-learning\UT\TC\Testlogdata.yaml")
    @unpack
    def _test_log003(self, **para):
        print(para)
        self.drive.find_element(By.NAME, "accounts").send_keys(para["user"])
        self.drive.find_element(By.NAME, "pwd").send_keys(para["pwd"])
        self.drive.find_element(By.XPATH, '//button[text()="登录"]').click()
        time.sleep(2)

    @data(*get_case())
    @unpack
    def test_log004(self, **para):
        print(para)
        self.drive.find_element(By.NAME, "accounts").send_keys(para["user"])
        self.drive.find_element(By.NAME, "pwd").send_keys(para["pwd"])
        self.drive.find_element(By.XPATH, '//button[text()="登录"]').click()
        time.sleep(2)




         # 断言：实际情况（页面获取）和期望情况（维护在数据当中）进行比较
        self.assertEqual("hami", "hami")
        self.assertMultiLineEqual('hami', 'hami')
        try:
            sj_result = self.drive.find_element(By.XPATH, "/ html / body / div[2] / div / ul[1] / div / div / em[2]").text
            qw_result = para["assert"]
            print(sj_result)
            print(qw_result)
        except:
            raise  # 抛出对应的异常
        else:
            assert qw_result in sj_result


    # def test_A(self):
    #     print("A")
    #
    # def test_002(self):
    #     print("002")

    # 执行顺序- 0-9 -<- A-Z -<- a-z ascii

if __name__ == '__main__':
    unittest.main()

































