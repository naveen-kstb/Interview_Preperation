# print the even number characters in the given string:

str = "Hello World"
print(str[1::2])

# Find the duplicate number in the given list:
l1 = [10, 20, 30, 10, 20, 50, 60, 30]
unique_list = []
duplicate_list = []
for i in l1:
    if i not in unique_list:
        unique_list.append(i)
    elif i not in duplicate_list:
        duplicate_list.append(i)

print(duplicate_list)


# Create a decorator function and made the given string in uppercase:
def lowercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.lower()

    return wrapper


@lowercase_decorator
def given_string(str):
    return str


str = "PYTHON"
lowercase_str = given_string(str)
print(lowercase_str)
