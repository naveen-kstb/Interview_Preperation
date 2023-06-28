# 1.
# s = "Name,  S1: 78, s2: 66, s3: 88"
# o/p: Name : Total marks
input_string = "Name, S1: 78, s2: 66, s3: 88"

# Splitting the input string by commas
parts = input_string.split(',')

# Extracting the name and marks
name = parts[0]
marks = [int(part.split(':')[1].strip()) for part in parts[1:]]

# Calculating the total marks
total_marks = sum(marks)

# Constructing the output string
output_string = f"{name}: {total_marks}"

# Printing the output
print(output_string)

# 2. Find the duplicate number in given list
l1 = [1, 2, 3, 1, 2, 42, 1, 3, 2, 42]

uniquelist = []
duplicatelist = []

for i in l1:
    if i not in uniquelist:
        uniquelist.append(i)
    elif i not in duplicatelist:
        duplicatelist.append(i)

print(duplicatelist)

# 3. Find the sum of diagonal of square matrix and it should not add same element twice.
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

n = len(matrix)
diagonal_sum = 0

for i in range(n):
    diagonal_sum += matrix[i][i]
    diagonal_sum += matrix[i][n - i - 1]

print("Sum of the diagonal elements:", diagonal_sum)

# 4. Check the given number is palindrome or not
num = int(input("Enter the Number: "))

temp = num
reverse_num = 0

while temp != 0:
    digit = temp % 10
    reverse_num = (reverse_num * 10) + digit
    temp //= 10

if num == reverse_num:
    print(num, "is Palindrome")
else:
    print(num, "is Not Palindrome")