import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
import sys
import time
sys.path.append('E:/Subash/Python/SeleniumAutomation/Unittest_PageObjectModel')

from pageObjects import LoginPage

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