#1. Write a Python code to reverse the whole word without using built-in methods
str = "All ships are busy at the dock"

reversed_str =""
word =[]
current_word =""
for char in str:
    if char ==" ":
        if current_word:
            word = [current_word] + word
            current_word =""
    else:
        current_word += char
if current_word:
    word = [current_word] + word
reversed_text =""
for i in range(len(word)):
    if i == 0:
        reversed_text += word[i]
    else:
        reversed_text = reversed_text + " " + word[i]

print("Actual input is: ", str)
print("reversed text is :", reversed_text)

#2. Write a Python code to reverse the whole word using built-in methods
str = "All ships are busy at the dock"
reversed_words =" ".join(str.split()[::-1])
print(reversed_words)