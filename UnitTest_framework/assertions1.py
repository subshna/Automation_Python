import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def test_Name1(self):
        self.driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')
        self.driver.get('https://www.google.com')
        pagetitle = self.driver.title

        self.assertEqual('Google', pagetitle, 'Webpage title is different')
        self.driver.close()

    def test_Name2(self):
        self.driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')
        self.driver.get('https://www.google.com')
        pagetitle = self.driver.title

        self.assertNotEqual('Google1', pagetitle, 'Webpage title is different')
        self.driver.close()

if __name__ == '__main__':
    unittest.main()