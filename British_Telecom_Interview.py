# WAP to replace the given list "bt", "ee" to airtel:
listA = ["bt", "ee", "orange"]
for i in range(len(listA)):
    if listA[i] == "bt" or listA[i] == "ee":
        listA[i] = "airtel"

print(listA)

# WAP to print the given list in new list:
l1 = ["bt", "ee", "orange"]
new_list = l1
print(new_list)

# WAP to remove the last two values in given tuple and print the rest in new tuple:
t1 = ("head", "tail", "body", "arms", "legs", "hands")
new_tuple = t1[:-2]
print(new_tuple)

# WAP to print the value of given dictionary:
d1 = {"name": "Naveen", "Des": "QA"}
print(d1.values())
