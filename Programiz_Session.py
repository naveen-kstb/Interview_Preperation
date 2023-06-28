# x = 5
# y = 10
#
# print('The value of x is {} and y is {}'.format(x, y))
#
# num = input("Enter a Number: ")
# print("You Entered: ", num)
# print("Data type of num: ", type(num))
# num = int(input('Enter a number: '))
# print("Data type of num: ", type(num))

# global_Var = 10
#
#
# def outer_function():
#     outer_var = 20
#
#     def inner_function():
#         inner_var = 30
#
#         print(inner_var)
#
#     print(outer_var)
#
#     inner_function()
#
#
# print(global_Var)
#
# outer_function()

global_var = 10


def my_function():
    local_var = 20

    global global_var
    global_var = 30


print(global_var)
my_function()
print(global_var)

i = 10
if i >= 10:
    print("Execute this if statement")
else:
    print("Execute the else statement")

# Reading File
try:
    file1 = open("test.txt", "r")  # with open("test.txt") as file1:
    read_Content = file1.read()
    print(read_Content)
finally:
    file1.close()

# Writing File

with open("test2.txt", "w") as file2:
    file2.write("My name is Naveen")
    file2.write("\nI have completed my B.E in ECE")
import os

print(os.getcwd())
print(os.listdir())
# os.remove("test2.txt")

# program to print the reciprocal of even numbers

try:
    num = int(input("Enter the Number: "))
    assert num % 2 == 0
except:
    print("Not an Even Number!")
else:
    reciprocal = 1 / num
    print(reciprocal)
