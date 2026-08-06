# WAP program to find the largest number and second-largest number in given input
input = ["212",24,762,3,12,0,"0","121",1]

numbers = [int(i) for i in input]
numbers.sort(reverse=True)

print("Largest Number is", numbers[0])
print("Second Largest Number is", numbers[1])

# Interviewer given the code and asked me to modify for the summ of odd numbers
input1 = [212,24,762,3,12,0,0,121,1]
def sum_even_numbers(numbers):
    total = 0
    for number in numbers:
        if number % 2 != 0:
            total += number
    return total

print(sum_even_numbers([1, 2, 3, 4, 5, 6]))

# Write a decorator example and explain
def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@decorator
def call():
    print("Hello")
call()