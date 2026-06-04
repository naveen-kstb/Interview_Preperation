#WAP to return the repeated character count as an output

input_string = "engineering"
output_string = ""
for char in input_string:
    if input_string.count(char) == 3 and char not in output_string:
        output_string += char

print(output_string)