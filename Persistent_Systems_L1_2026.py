# Write a simple Python code for the number of occurrence as per the below input and output
# input : " Python Selenium Python Api"
# Output : Python -2
# Selenium -1
# Api - 1
text = "Python Selenium Python Api"

words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"{word} - {count}")
#-----------------------------------------------------------------------------------
# Using Counter module way from python collections
from collections import Counter
text = "Python Selenium Python Api"
word_count = Counter(text.split())

for word, count in word_count.items():
    print(f"{word} - {count}")

# 2. Write a Python code to get the output as duplicates present in the given input number
# input : [1,2,3,2,4,5]
# output : duplicate presents
numbers = [1, 2, 3, 2, 4, 5]

duplicates = [num for num in set(numbers) if numbers.count(num) > 1]

if duplicates:
    print(f"duplicate presents: {duplicates}")
else:
    print("no duplicate presents")