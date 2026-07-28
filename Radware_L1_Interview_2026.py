# Explain the logic for Fibonacci series and write a code

num = int(input("Enter a number: "))

a, b = 0, 1
while a < num:
    a, b = b, a+b

if a == num:
    print("Yes")
else:
    print("No")