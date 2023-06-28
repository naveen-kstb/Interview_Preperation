# Write a Python program that reverses a string and checks if the repeated characters form a palindrome or not:
def reverse_string(string):
    # Reverses the given string
    return string[::-1]


def check_palindrome(string):
    # Removes non-alphabetic characters and converts to lowercase
    string = ''.join(char.lower() for char in string if char.isalpha())

    # Reverses the cleaned string
    reversed_string = reverse_string(string)

    # Checks if the reversed string is equal to the original string
    if reversed_string == string:
        return True
    else:
        return False


def check_repeated_characters_palindrome(string):
    # Removes non-alphabetic characters and converts to lowercase
    string = ''.join(char.lower() for char in string if char.isalpha())

    # Checks if the cleaned string is a palindrome
    if check_palindrome(string):
        # Creates a dictionary to count the occurrences of each character
        char_count = {}
        for char in string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # Checks if any character occurs more than once
        for count in char_count.values():
            if count > 1:
                return True

        return False
    else:
        return False


# Test the functions
input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)

if check_repeated_characters_palindrome(input_string):
    print("The repeated characters form a palindrome.")
else:
    print("The repeated characters do not form a palindrome.")


# Write a Python program that finds the unique elements in a given list using the set data type:

def find_unique_list(input_list):
    unique_set = set(input_list)
    unique_list = list(unique_set)
    return unique_list


# Test the function
input_list = [1, 2, 3, 2, 4, 4, 5, 3, 5, 6]
unique_list = find_unique_list(input_list)

print("Unique elements in the list:", unique_list)

# Write a Selenium Script to open google page in cross browser (Chrome and Firefox):
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

Service_obj = Service(r"C:\Users\naveen.kstb\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=Service_obj)

driver.get("https://www.google.com/")
driver.quit()

Service_obj = Service(r"C:\Users\naveen.kstb\Downloads\geckodriver-v0.32.2-win64\geckodriver.exe")
driver = webdriver.Firefox(service=Service_obj)

driver.get("https://www.google.com/")
driver.quit()
