# Write a Python program for below 2 list and get the output as mentioned
l1 = ["a", "b", "c", "d"]
l2 = [3,2,1,4]
# Output = [c,b,a,d]
n = len(l2)
resu = []
for i in range(1, n + 1):
    for j in range(n):
        if l2[j] == i:
            resu.append(l1[j])

print(resu)

# 2. Write a program to reverse the string without using any built-in methods
text = "python"
reversed_text =""
for char in text:
    reversed_text = char + reversed_text

print(reversed_text)