import unittest
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_xd(unittest.TestCase):

    # 业务流程：打开网站 注册 登录 下单 关闭网址
    @classmethod
    def setUpClass(cls) -> None:
        print("我只会执行当前类-打开")

    @classmethod
    def tearDownClass(cls) -> None:
        print("我只会执行当前类-关闭")

    def setUp(self) -> None:
        print("每个用例都会执行一次-开始")
        # self.drive = webdriver.Chrome()
        # self.url = "https://www.baidu.com/"
        # self.drive.get(self.url)
        # self.drive.implicitly_wait(10)

    # 每个测试用例之后关闭网页
    def tearDown(self) -> None:
        print("每个用例都会执行一次-结束")
        # self.drive.quit()

    def test_zc(self):
        # 注册
        print("我是注册")

    def test_login(self):
        # 登录
        print("我是登录")

    def test_xd(self):
        # 下单
        print("我是下单")


if __name__ == '__main__':
    unittest.main()










































































