#Write a python program to convert 2025-07-12 to 12 July ?
from datetime import datetime
date = "2025-07-12"

d = datetime.strptime(date, "%Y-%m-%d")

out = d.strftime("%d %B")
print(out)


# Take a list of strings, return true if any of the value has punctuation in it?
# Use inbuilt function to get output.

import string

list = ["Naveen", "Python", "Good evening"]

out = any(any(char in string.punctuation for char in word) for word in list)
print(out)

# Print the countries with index. List - [England, Scotland, Ireland, Wales]
# o / p -
# 1, England
# 2, Scotland
# 3, Ireland
# 4, Wales
List = ["England", "Scotland", "Ireland","Wales"]

for i in range(len(List)):
    print(i + 1, List[i])

