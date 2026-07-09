# Write a Python code for below input and output  Input:  "I am Naveen" Output : "n ee vaNmai"

# Step 1: Take input
sentence = "I am Naveen"

# Step 2: Find space positions from original string
space_positions = []
for i in range(len(sentence)):
    if sentence[i] == " ":
        space_positions.append(i)

print("Space positions:", space_positions)  # [1, 4]

# Step 3: Remove spaces and build plain string
plain = ""
for char in sentence:
    if char != " ":
        plain += char

print("Without spaces:", plain)  # IamNaveen

# Step 4: Reverse the plain string
reversed_plain = ""
for char in plain:
    reversed_plain = char + reversed_plain

print("Reversed plain:", reversed_plain)  # neeevaNmaI

# Step 5: Insert spaces back at same positions
result = ""
plain_index = 0
for i in range(len(sentence)):
    if i in space_positions:
        result += " "          # Put space at same position
    else:
        result += reversed_plain[plain_index]  # Put reversed char
        plain_index += 1

print("Input  :", sentence)
print("Output :", result)

