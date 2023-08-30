from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()

driver.switch_to.frame("packageListFrame")  # First Frame
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
driver.switch_to.default_content()
time.sleep(5)

driver.switch_to.frame("packageFrame")  # Second Frame
driver.find_element(By.LINK_TEXT, "WebDriver").click()
driver.switch_to.default_content()
time.sleep(5)

driver.switch_to.frame("classFrame")   # Third Frame
driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[6]/a").click()
time.sleep(5)