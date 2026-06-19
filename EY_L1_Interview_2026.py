# 1. Find first non repeated character from String.

from collections import Counter

s = "aabbbcde"

char_count = Counter(s)

for char in s:
    if char_count[char] == 1:
        print(f"First non-repetitive character: {char}")
        break

# 2. Find the duplicate number in the given list
L1 =[1,2,3,2,4,1]
Unique_list = []
duplicate_list = []
for i in L1:
    if i not in Unique_list:
        Unique_list.append(i)
    elif i not in duplicate_list:
        duplicate_list.append(i)

print(duplicate_list)


