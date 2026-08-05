# WAP to count the repeated character in the given sting without using built-in method

string = "Naveenkumar"
char_counts ={}

for char in string:
    if char == "N":
        key = "n"
    else:
       key = char

    if key in char_counts:
        char_counts[key] +=1
    else:
        char_counts[key] = 1

for key in char_counts:
    if char_counts[key] > 1:
        print(f"{key} - {char_counts[key]}")
