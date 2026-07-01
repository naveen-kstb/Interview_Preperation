#1. Write a Python code input as yyyy/mm/dd format and output as dd/mm/yyyy format
# Step 1: Take user input
date = input("Enter date in yyyy/mm/dd format: ")

# Step 2: Separate yyyy, mm, dd manually
yyyy = ""
mm = ""
dd = ""
part = 1  # 1=year, 2=month, 3=day

# Step 3: Loop through each character
for char in date:
    if char == "/":
        part += 1  # Move to next part
    elif part == 1:
        yyyy += char  # Build year
    elif part == 2:
        mm += char    # Build month
    elif part == 3:
        dd += char    # Build day

# Step 4: Rearrange to dd/mm/yyyy format
result = dd + "/" + mm + "/" + yyyy

print("Output :", result)

# Take a list of numbers and find the 3rd largest one from the list
l1 = [10,20,3,40,5,60]

uni_sorted = sorted(list(set(l1)), reverse= True)

if len(uni_sorted) >= 3:
    third_largest = uni_sorted[2]
    print("third largest:", third_largest)
else:
    print("list is not have 3 unique values")
