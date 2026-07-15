# Input [0,1,0,1,1,0] output should be [0,0,0,1,1,1] in python

arr = [0, 1, 0, 1, 1, 0]
result = [x for x in arr if x == 0] + [x for x in arr if x == 1]
print(result)

# s = 'apple,orange,mango,apple,banana,,mango,sapota,mango'  count the repeated words
s = 'apple,orange,mango,apple,banana,mango,sapota,mango'
fruits = s.split(',')
result = {}
for fruit in fruits:
    key = fruit.capitalize()
    result[key] = result.get(key,0) + 1
print(result)

# Give me an example of Exception

counts = {'apple': 2, 'mango': 3}  # Example dictionary

try:
    # This will fail because 'pineapple' is not in the dictionary
    print(counts['pineapple'])
except KeyError as e:
    print(f"Error: The key {e} was not found in the dictionary!")