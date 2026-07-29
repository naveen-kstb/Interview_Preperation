# Write a program to find the closest number pair from the given list:
list1 = [10,1,11,100,98,56,74]
min_diff = float('inf')
pair =()

for i in range(len(list1)):
    for j in range(i +1, len(list1)):
        diff = abs(list1[i] - list1[j])
        if diff < min_diff:
            min_diff = diff
            pair = (list1[i], list1[j])
print("Closest Number is: ", pair[0], pair[1])

# What would be the output of below code:
str1 = "python"
str2 = "python1"
str1[3] = "r"
print(str1)  # Output:TypeError: 'str' object does not support item assignment

