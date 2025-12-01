from selenium import webdriver
import time


driver = webdriver.Chrome()  # client library

# driver.get('https://github.com/therash08')
# time.sleep(6)

# driver.get('https://google.com')

driver.get('https://daraz.com')
driver.maximize_window()

time.sleep(10)
