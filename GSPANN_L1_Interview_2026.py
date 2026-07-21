# WAP to remove the vowels letters in the given string

name ="James"

result =""
for char in name:
    if char.lower() not in "aeiou":
        result += char

print(result)

