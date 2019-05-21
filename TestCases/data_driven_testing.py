from modules import xlUtils
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')

driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()

xlpath = ('../Resources/Test_data.xlsx')

totalrow = xlUtils.getRowCount(xlpath, 'Sheet1')

for r in range(2, totalrow+1):
    username = xlUtils.readData(xlpath, 'Sheet1', r, 1)
    passwd = xlUtils.readData(xlpath, 'Sheet1', r, 2)

    driver.find_element_by_name('txtUsername').send_keys(username)
    driver.find_element_by_name('txtPassword').send_keys(passwd)
    driver.find_element_by_name('Submit').click()

    if driver.current_url == 'https://opensource-demo.orangehrmlive.com/index.php/dashboard':
        print ('Test Passed')
        xlUtils.writeData(xlpath, 'Sheet1', r, 3, 'Test Passed')
        driver.find_element_by_id('welcome').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="welcome-menu"]/ul/li[2]/a').click()
    else:
        print ('Test Failed')
        xlUtils.writeData(xlpath, 'Sheet1', r, 3, 'Test Failed')

driver.close()
driver.quit()