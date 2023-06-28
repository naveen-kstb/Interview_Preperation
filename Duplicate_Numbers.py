l1 = [2, 3, 5, 7, 2, 8, 6, 9, 45, 23, 3, 10, 7, 9, 6]

uniquelist = []
duplicateList = []

for i in l1:
    if i not in uniquelist:
        uniquelist.append(i)
    elif i not in duplicateList:
        duplicateList.append(i)

print(duplicateList)

X = lambda a, b: a * b
print(X(5, 4))
