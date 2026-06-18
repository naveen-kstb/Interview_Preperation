#WAP to return the repeated character count as an output

input_string = "engineering"
output_string = ""
for char in input_string:
    if input_string.count(char) == 3 and char not in output_string:
        output_string += char

print(output_string)

# I am in main tab i have to do some performance on a new tab and then come back to main tab how can i
# achieve this through selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

main_tab = driver.current_window_handle
driver.execute_script("window.open('https://www.google.com/', '_blank')")
driver.switch_to.window(driver.window_handles[-1])
print("New Tab title:" , driver.title)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.NAME, "q")))
print("Search box visible on new tab")
driver.switch_to.window(main_tab)
print("Back to main tab", driver.title)
driver.quit() 