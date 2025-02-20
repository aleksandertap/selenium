from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(2)
print("Title:", driver.title)
search_bar = driver.find_element(By.NAME,"q")
if(search_bar):
    print("Search bar found")


search_bar.send_keys("Selenium WebDriver")
search_bar.send_keys(Keys.RETURN)

time.sleep(3)

driver.quit()