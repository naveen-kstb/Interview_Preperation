count = 0

my_string = "NaveenKumar"
my_char = "a"

for i in my_string:
    if i == my_char:
        count += 1

print(count)

# Using method count()

print(my_string.count(my_char))


# Number of occurrence using integers
count = 0
my_integer = [1, 2, 5, 2, 1, 6, 7, 2, 1, 8, 1, 10, 1, 15, 16]
my_occ = 1

print(my_integer.count(my_occ))
