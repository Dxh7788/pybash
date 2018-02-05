import unittest
from selenium import webdriver
from time import sleep


class LoginCase(unittest.TestCase):

    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.maximize_window()


    #定义登录
    def login(self,username,password):
        self.dr.get('https://sit.test.htouhui.com/memberLoginPage')
        self.dr.find_element_by_id('username').send_keys(username)
        self.dr.find_element_by_id('password').send_keys(password)
        self.dr.find_element_by_id('butt').click()

    def test_login_success(self):
        self.login('h3168039689','123abc')
        sleep(3)

    def tearDown(self):
        sleep(2)
        print('自动测试完毕！')
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
