# 1. Python - factorial of a number.


num = int(input("Enter a number: "))

factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print("The factorial of", num, "is", factorial)


# 2. Reverse the string:
def reverse_string(str):
    str1 = ""
    for i in str:
        str1 = i + str1
    return str1


str = "Naveen Kumar"

print("The original string is: ", str)
print("The reversed string is: ", reverse_string(str))

# Using Method
str = "Naveen Kumar"[::-1]
print(str)

# 3. To find prime numbers between 1-10:
prime_numbers = []

for num in range(2, 10):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)

print(prime_numbers)

# 4. Write a selenium script to login Amazon wesite and  Search for skullcandy headset Bluetooth price from 1000-2000
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

Service_obj = Service(r"C:\Users\naveen.kstb\Downloads\geckodriver-v0.32.2-win64\geckodriver.exe")
driver = webdriver.Firefox(service=Service_obj)

driver.get("https://www.amazon.in/")
driver.maximize_window()

driver.find_element(By.ID, "twotabsearchtextbox").send_keys("skullcandy headset Bluetooth")
time.sleep(5)
# driver.find_element(By.XPATH, "//div[@aria-label='skullcandy headphones bluetooth']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located(
    (By.XPATH, "//div[@aria-label='skullcandy headphones bluetooth']"))).click()
# rate = driver.find_element(By.XPATH, "//span[@class='a-price-whole']")

a = ActionChains(driver)
m = driver.find_element(By.LINK_TEXT, "₹1,000 - ₹5,000")
time.sleep(5)
a.move_to_element(m).click()

# driver.find_element(By.XPATH, "//span[contains(text(),'₹1,000 - ₹5,000')]").click()
driver.close()
