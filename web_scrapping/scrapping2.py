from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


driver.get("https://www.google.com")  #
time.sleep(3)

try:
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Web Scraping")
    print("সার্চ বক্সে টেক্সট লেখা হলো।")

    print(f"পেজের বর্তমান টাইটেল: {driver.title}")

except Exception as e:
    print(f"একটি সমস্যা হয়েছে: {e}")

finally:
    driver.quit()
