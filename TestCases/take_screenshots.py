from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')

driver.get('http://newtours.demoaut.com')
driver.maximize_window()

driver.save_screenshot('../CaptureScreen/homepage.png')
driver.get_screenshot_as_file('../CaptureScreen/homepage2.png')

driver.quit()