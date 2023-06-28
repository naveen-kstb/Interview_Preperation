num = int(input("Enter the Number: "))


def is_even(num):
    return num % 2 == 0


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


if is_even(num):
    print(num, "is even")
else:
    print(num, "is odd")

if is_prime(num):
    print(num, "is prime")
else:
    print(num, "is not prime")
