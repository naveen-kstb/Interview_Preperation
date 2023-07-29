# 1. Write a python code to remove the duplicates in given string:
input_string = "olpkttsozxvopdkl"
output_string = ""

for char in input_string:
    if char not in output_string:
        output_string += char

print(output_string)

# 2.Write a syntax for implicit and explicit wait:
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver = webdriver.Chrome()
#
# driver.implicitly_wait(10)
#
# element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((""))
