import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Baidu(unittest.TestCase):

    # 每个测试用例之前打开网页
    def setUp(self) -> None:
        self.drive = webdriver.Chrome()
        self.url = "https://www.baidu.com/"
        self.drive.get(self.url)
        self.drive.implicitly_wait(10)

    # 每个测试用例之后关闭网页
    def tearDown(self) -> None:
        self.drive.quit()



    # 测试用例一定要用test开头，否则unittest无法识别
    def test_001(self):

        # 用显示等待去定位元素
        # 导包 实例化参数 调用方法
        input_text = (By.ID, "kw")
        ok_button = (By.ID, "su")
        input_ele = WebDriverWait(self.drive, 10).until(EC.presence_of_element_located(input_text))
        button = WebDriverWait(self.drive, 10).until(EC.presence_of_element_located(ok_button))
        input_ele.send_keys("hello")
        button.click()

    def test002(self):

        # 用显示等待去定位元素
        # 导包 实例化参数 调用方法
        input_text = (By.ID, "kw")
        ok_button = (By.ID, "su")
        input_ele = WebDriverWait(self.drive, 10).until(EC.presence_of_element_located(input_text))
        button = WebDriverWait(self.drive, 10).until(EC.presence_of_element_located(ok_button))
        input_ele.send_keys("hahaha")
        button.click()

    def test003(self):

        # 用显示等待去定位元素
        # 导包 实例化参数 调用方法
        input_text = (By.ID, "kw")
        ok_button = (By.ID, "su")
        input_ele = WebDriverWait(self.drive, 10).until(EC.presence_of_element_located(input_text))
        button = WebDriverWait(self.drive, 10).until(EC.presence_of_element_located(ok_button))
        input_ele.send_keys("selenium")
        button.click()





if __name__ == '__main__':
    unittest.main  # 调用方法执行测试用例，此方法会搜索该模块下所有以test开头的测试用例并自动执行
































