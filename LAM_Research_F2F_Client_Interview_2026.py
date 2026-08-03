# Input = [2,3,7,0,4,0,0,0] and i want the output as [2, 3, 7, 4, 0, 0, 0, 0] WAP

nums = [2,3,7,0,4,0,0,0]

result = []

# Add non-zero elements
for num in nums:
    if num != 0:
        result.append(num)

# Add zeros
while len(result) < len(nums):
    result.append(0)

print(result)