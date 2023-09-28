# Write a lambda expression with example:
mul = lambda a, b: a * b
print(mul(5, 2))

# WAP to print the number diagonal pattern:
n = 3
num = 1

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    print(num, end="")
    num += 1

    for j in range(2 * i - 3):
        print(" ", end="")

    if i > 1:
        print(num, end="")
        num += 1
    print()

# WAP to check given number is prime or not:
num = int(input("Enter the number: "))
for i in range(2, num):
    if num % i == 0:
        print("Entered the number is not a prime number")
        break
else:
    print("Entered the number is a prime number")

# WAP to print the number 1 to 6 using while loop:
i = 1
while i < 6:
    print(i)
    i += 1


# Write a python program example of inheritance:
class student:
    def std_name(self):
        print("First Program")


class staff(student):
    def staff_name(self):
        print("another statement")


obj = staff()
obj.std_name()
obj.staff_name()
