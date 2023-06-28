d = {'a': 5, 'b': 3, 'c': 4, 'd': 1, 'e': 2}

output = ",".join([f"{key}{value}" for key, value in sorted(d.items(), key=lambda x: x[1])])

print(output)


# define  a python function inside that 2 method as valid and 2 method as invalid:
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_prime_numbers(lower, upper):
    prime_numbers = []
    for num in range(lower, upper + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers


def valid_method_1():
    return "This is a valid method."


def valid_method_2():
    return "This is another valid method."


def invalid_method_1():
    return "This method is invalid."


def invalid_method_2():
    return "This method is also invalid."


# Testing the methods
print(valid_method_1())
print(valid_method_2())
print(invalid_method_1())
print(invalid_method_2())

# Finding prime numbers between 1 and 10
lower = 1
upper = 10
prime_numbers = get_prime_numbers(lower, upper)
print(prime_numbers)
