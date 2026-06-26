# Write a Python program to check the given 2 string is anagram or not:

def is_anagram_sorted(str1, str2):
    clean_str1 = str1.replace(" ", "").lower()
    clean_str2 = str2.replace(" ", "").lower()

    return sorted(clean_str1) == sorted(clean_str2)


word1 = "Listen"
word2 = "Silent"

if is_anagram_sorted(word1, word2):
    print(f"'{word1}' and '{word2}' are anagrams.")
else:
    print(f"'{word1}' and '{word2}' are NOT anagrams.")

# Write a fixtures function and invoke the browser:
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome
    driver.maximize_window()

    yield driver


driver.quit()
