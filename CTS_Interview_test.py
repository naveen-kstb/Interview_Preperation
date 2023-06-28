# Find the last character is n in the given string if it is there print True:
string = "Naveen"
if string[-1] == "n":
    print("True")
else:
    print("False")

# Find the Number of occurance in the given string:
string = "Naveen"
print(string.count("e"))


# Define a function and add two numbers:
def sum_numbers(a, b):
    return a + b


result = sum_numbers(10, 20)
print(result)


# Define a function and check the count of occurrence in given string:
def count_occurances(stringA, stringB):
    return stringA.count(stringB)


stringA = "qwertyuiopiopiopu"
stringB = "iop"

occurance = count_occurances(stringA.lower(), stringB.lower())

print(f"The number of occurrences of '{stringB}' in '{stringA}' is: {occurance}")

# Write a selenium script to open gmail and click signup and enter the name in First name field:
# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# Service_obj = Service(r"C:\Users\naveen.kstb\Downloads\chromedriver_win32\chromedriver (2).exe")
# driver = webdriver.Chrome(service=Service_obj)
#
# driver.get("https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp")
# driver.maximize_window()
# time.sleep(5)
# driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys("Naveen Kumar")

# Write a test case in pytest and assert that condition and try to skip that testcase:
import pytest

# import pytest
# import unittest
#
#
# @pytest.mark.skip
# def test_one():
#     i = 5
#     print(i)
#     assert i == 5
#
#
# class TestSum(unittest.TestCase):
#
#     def test_sum(self):
#         self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
#
#     def test_sum_tuple(self):
#         self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")\

# Technical round - 2
import openpyxl

input_file = r"C:\Users\naveen.kstb\Desktop\PythonDemo1.xlsx"
output_file = r"C:\Users\naveen.kstb\Desktop\PythonDemo1.xlsx"

workbook = openpyxl.load_workbook(input_file)
sheet = workbook.active
sheet['A3'] = "Siva Shankar"

new_row = ["Naveen", "Unknown", "Unknown"]
sheet.append(new_row)

workbook.save(output_file)
print(f"XLSX file '{output_file}' has been successfully created with the modification")
