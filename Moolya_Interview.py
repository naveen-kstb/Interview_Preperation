# 1. Open a Chrome browser
# 2. In search window type selenium
# 3. In the below suggestion check if there is selenium webdriver then click on it
# 4. Then it should redirect to that selenium webdriver page


import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Service_obj = Service(r"C:\Users\naveen.kstb\Downloads\geckodriver-v0.32.2-win64\geckodriver.exe")  #("C:\\Users\\naveen.kstb\\Downloads\\chromedriver_win32\\chromedriver.exe")
# driver = webdriver.Firefox(service=Service_obj)
#
# driver.get("https://www.google.com/")
# driver.maximize_window()
#
# driver.find_element(By.ID, "APjFqb").send_keys("Selenium")
# time.sleep(4)
# message = driver.find_element(By.XPATH, "//*[@aria-label='selenium tutorial']")
# time.sleep(4)
#
# if message == message:
#     message.click()
# else:
#     print("Not there in given suggestion")


Service_obj = Service(r"C:\Users\naveen.kstb\Downloads\geckodriver-v0.32.2-win64\geckodriver.exe")
driver = webdriver.Firefox(service=Service_obj)

driver.get("https://www.google.com/")
driver.maximize_window()

driver.find_element(By.ID, "APjFqb").send_keys("Selenium")
time.sleep(3)
message = driver.find_element(By.ID, "jZ2SBf")
time.sleep(3)

if message == message:
    message.click()
else:
    print("Not there in given suggestion")

driver.switch_to.alert.accept()