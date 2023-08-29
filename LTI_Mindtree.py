# WAP how many times given string repeated in dictionary format:
# string = "Naveen"
# char_count = {}
# for char in string:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
#
# for char, count in char_count.items():
#     print(f"The Number '{char}' is repeated '{count}' times.")


# WAP for decorator function take any example as you need:

def add_decorator(func):
    def wrapper(a, b):
        print("Adding two numbers:", a, "+", b)
        result = func(a, b)
        print("Result:", result)
        return result

    return wrapper


@add_decorator
def add_numbers(a, b):
    return a + b


num1 = 10
num2 = 20
result = add_numbers(num1, num2)
