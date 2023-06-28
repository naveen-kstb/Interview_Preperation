# i = 6
#
# while i==6:
#     print("Value of i is" +str(i))


depth = 6
for number in range(1, depth):
    for i in range(1, number + 1):
        print(i, end=' ')
    print("")


def diamond(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")

        print("")


n = 6
diamond(n)
