# WAP code to get assertions for the given response
import numbers

respose = {
    "name" : "Naveen",
    "Age" : 30,
    "Status" : "Active"
 }

assert respose["name"] != "", "Name Should not be Blank"
assert respose["Age"] > 18,   "Age Should be greater than 18"
assert respose["Status"]== "Active", "Status should be Active"
print("All assertions passed")

# WAP code to find the second-largest unique value in the given input
numbers = [10, 30, 60, 20, 60, 50, 40 ]
largest = second = float('-inf')
for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif largest > num > second:
        second = num

print("The Second-Largest Unique Number is: ", second)