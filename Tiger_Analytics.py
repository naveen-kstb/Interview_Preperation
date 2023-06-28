# Diamond Pattern Program:
rows = int(input("Enter the number of rows: "))
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
k = rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")

# Selenium script enter amazon website and click on signin
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Service_obj = Service(r"C:\Users\naveen.kstb\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=Service_obj)

driver.get("https://www.amazon.in/")

driver.find_element(By.ID, "nav-link-accountList-nav-line-1").click()
