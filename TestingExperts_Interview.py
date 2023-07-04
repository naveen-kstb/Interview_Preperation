# Write a selenium script to find xpath for first name and pass your name into it
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rpachallenge.com/")
driver.maximize_window()

time.sleep(3)
driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelFirstName']").send_keys("Naveen")
time.sleep(3)

# Write a Python program take a input string from user and count each character repeated how many times:
#
# input_string = input("Enter the string: ")
# string = input_string.lower()
# char_counts = {}
#
# for char in string:
#     if char.isalpha():
#         if char in char_counts:
#             char_counts[char] += 1
#         else:
#             char_counts[char] = 1
#
# for char, count in char_counts.items():
#     print(f"The character '{char}' is repeated '{count}' times.")

# Write a decorator function example:
# def lowercase_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.lower()
#
#     return wrapper
#
#
# @lowercase_decorator
# def string(str):
#     return str
#
#
# str = "PYTHON INTERVIEW"
#
# lowercase_str = string(str)
# print(lowercase_str)