import unittest
from selenium import webdriver

class Test(unittest.TestCase):

    def test_name1(self):
        driver = webdriver.Chrome('../driver/chromedriver.exe')
        driver.get('https://www.google.com')
        pageTitle = driver.title

        self.assertTrue(pageTitle == 'Google', 'Passed')
        driver.close()

    def test_name2(self):
        driver = webdriver.Chrome('../driver/chromedriver.exe')
        driver.get('https://www.google.com')
        pageTitle = driver.title

        self.assertFalse(pageTitle == 'Google123', 'Passed')
        driver.close()

if __name__ == '__main__':
    unittest.main()