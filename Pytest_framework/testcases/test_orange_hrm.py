from selenium import webdriver
import pytest

class TestOrangeHRMApp():

    @pytest.yield_fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        yield
        self.driver.close()

    def test_homePage(self, setup):
        assert self.driver.title == 'OrangeHRM'

    def test_login(self, setup):
        self.driver.find_element_by_name('txtUsername').send_keys('Admin')
        self.driver.find_element_by_name('txtPassword').send_keys('admin123')
        self.driver.find_element_by_name('Submit').click()
        assert self.driver.title == 'OrangeHRM'

if __name__ == '__main__':
    pytest.main()