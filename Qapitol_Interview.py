# WAP to reverse the string:
# def reverse_string(str):
#     str1 = ""
#
#     for i in str:
#         str1 = i + str1
#     return str1
#
#
# str = "Python Programming"
#
# print("The actual string is: ", str)
# print("The reversed string is: ", reverse_string(str))

# Remove the duplicate in Given string:

str = "Naveen Kumar" + "\nHello"
result = ""
for i in str:
    if i not in result:
        result += i

print(result)
