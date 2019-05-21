from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')

driver.get('https://www.amazon.in')
driver.maximize_window()

# Capture all the cookies created by browser
allCookies = driver.get_cookies()
print (len(allCookies))
print (allCookies)

# adding new cookies to browser
new_cookie = {'name':'MyCookie', 'value':'1234567890'}
driver.add_cookie(new_cookie)

# Capture all the cookies created by browser
allCookies = driver.get_cookies()
print (len(allCookies))
print (allCookies)

# Delete the cookie
driver.delete_cookie('MyCookie')
allCookies = driver.get_cookies()
print (len(allCookies))
print (allCookies)

# Delete all the Cookies
driver.delete_all_cookies()
allCookies = driver.get_cookies()
print (len(allCookies))

driver.close()
driver.quit()