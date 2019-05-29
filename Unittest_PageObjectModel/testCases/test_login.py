import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
import time
from pageObjects.LoginPage import LoginPage

class LoginTest(unittest.TestCase):
    baseUrl = 'http://admin-demo.nopcommerce.com'
    username = 'admin@yourstore.com'
    password = 'admin'
    driver = webdriver.Chrome('../drivers/chromedriver.exe')

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseUrl)
        cls.driver.maximize_window()

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)

        self.assertEqual('Dashboard / nopCommerce administration', self.driver.title,
                         'webpage title not matched')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='../reports'))