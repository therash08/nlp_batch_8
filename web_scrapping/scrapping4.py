from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. Start the WebDriver (Opens Chrome window)
# Selenium Manager handles the driver installation automatically
driver = webdriver.Chrome()

# 2. Target URL (A site that requires interaction)
# We will use Google to demonstrate typing into a search box
driver.get("https://www.google.com")

try:
    # 3. Wait for the element to be visible (A key dynamic scraping step)
    # Wait for a maximum of 10 seconds until the search box is present
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    # 4. Perform an action (Simulate a user typing)
    search_box.send_keys("This is rash")
    print("✅ Successfully typed text into the search box.")

    # Wait briefly to see the result
    time.sleep(6)

    # 5. Extract the final title after interaction
    print(f"Page Title after interaction: {driver.title}")

except Exception as e:
    print(f"❌ An error occurred during the dynamic scrape: {e}")

finally:
    # 6. Close the browser
    driver.quit()
    print("Browser closed.")
