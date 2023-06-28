# Palindrome Using String

string = input("Enter a letter: ")

if string == string[::-1]:
    print("The letter is Palindrome")
else:
    print("The letter is Not Palindrome")

# Palindrome Using Integer
num = int(input("Enter a value:"))
temp = num
reverse_num = 0
while temp != 0:
    digit = temp % 10
    reverse_num = (reverse_num * 10) + digit
    temp //= 10
if num == reverse_num:
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome number")
