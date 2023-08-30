from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()

driver.find_element(By.XPATH, "//div[@id='Tabbed']/a/button").click()

print(driver.current_window_handle)  # Current Window =0DB6780A31F6C22C44F36E2A99F894A4 - Parent
handles = driver.window_handles  # It returns all the handle values of opened browser window

for handle in handles:
    driver.switch_to.window(handle)
    time.sleep(5)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close()

driver.quit()
