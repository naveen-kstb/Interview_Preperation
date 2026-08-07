# WAP find the repeated number in given list
num =  [1,2,1,1,3,4,2]
out = max(num, key = num.count)
print(out)

# Added 2 in the above list and to get the 2 repeated numbers
nums =  [1,2,1,1,3,4,2,2]
count = {}

for num in nums:
    count[num] = count.get(num, 0) + 1

max_count = max(count.values())
result = [k for k, v in count.items() if v == max_count]
print(result)