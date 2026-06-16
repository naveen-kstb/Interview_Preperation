# 1. Description: Write a Python function fizz_buzz(n) that takes an integer n and returns a list of strings representing
# the numbers from 1 to n.  However, for multiples of three, append "Fizz" instead of the number,for multiples
# of five append "Buzz", and for numbers which are multiples of both three and five, append "FizzBuzz".
# >> > fizz_buzz(15)
# ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

print(fizz_buzz(15))

# 2. Every 4 years we have a leap year - we have one extra day (February 29). This occurance corrects the
# calendar because the rotation of the planet around the Sun takes approcimately 365.25 days.
#  In the Gregorian calendar there are 3 conditions to determine if a year contains a leap day.
# The year can be evenly devided by 4,
# unless: If the year can also be evenly devided by 100 it is NOT a leap year,
# unless: The year is also evenly devisible by 400. Then it is a leap year
# Write a function that returns a boolean based on is the year leap or not.

def is_gregorian_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

user_input = int(input("Enter a year: "))

if is_gregorian_leap_year(user_input):
    print(f"{user_input} is a Leap year")
else:
    print(f"{user_input} is NOT a Leap year")

