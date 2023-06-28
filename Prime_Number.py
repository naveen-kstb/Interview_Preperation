
num = int(input("Enter a number: "))

for i in range(2, num):
    if num % i == 0:
        print("Given Number is Not Prime")
        break
else:
    print("Given Number is Prime")

