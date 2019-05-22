import unittest
from selenium import webdriver

class SearchEnginesTest(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')
        self.driver.get('https://www.google.com')
        print ('Title of page', self.driver.title)
        self.driver.close()

    def test_bing(self):
        self.driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')
        self.driver.get('https://bing.com')
        print ('Title of page', self.driver.title)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()