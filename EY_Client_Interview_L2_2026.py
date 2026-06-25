# Write a decorator function and explain:
def decorator(func):
    def wrapper():
        print("before execution")
        func()
        print("After execution")
    return wrapper

@decorator
def exe():
    print("execution")

exe()

# Write a Lambda Function and Explain
mul = lambda a,b : a *b
print(mul(2,3))

# Compare the below 2 lists using if condition and see what would be the output
l1 = [1,2,3,4,5]
l2 = [5,4,3,2,1]
if l1 == l2:
    print("Both the lists are equal")
else:
    print("Both the lists are not equal")

# Take any example and Write a nested dictionary example
# Initializing a multi-level dictionary
employees = {
    "emp1": {"name": "Naveen", "role": "Automation", "skills": ["Python", "Selenium"]},
    "emp2": {"name": "Dev", "role": "Developer", "skills": ["Python", "SQL"]}
}
for emp_id, info in employees.items():
    print(f"Employee ID: {emp_id}")
    for key, value in info.items():
        print(f"  {key}: {value}")

