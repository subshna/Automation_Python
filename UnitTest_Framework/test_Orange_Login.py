from selenium import webdriver
import unittest
from pyunitreport import HTMLTestRunner

class OrangeHRM_Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('../driver/chromedriver.exe')
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def test_verify_homepage(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.assertEqual('OrangeHRM', self.driver.title, 'Webpage not matched')

    def test_login(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.driver.find_element_by_name('txtUsername').send_keys('Admin')
        self.driver.find_element_by_name('txtPassword').send_keys('admin123')
        self.driver.find_element_by_name('Submit').click()
        self.assertEqual('OrangeHRM', self.driver.title, 'Webpage not matched')

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='../Reports'))