import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def test_name1(self):
        driver = None
        self.assertIsNone(driver, 'driver is None')

    def test_name2(self):
        driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')
        self.assertIsNotNone(driver, 'driver is Not None')
        driver.close()

if __name__ == '__main__':
    unittest.main()