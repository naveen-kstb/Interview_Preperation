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
