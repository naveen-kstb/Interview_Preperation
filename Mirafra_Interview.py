#1.
#output:
# 1
# 21
# 123
# 4321
# 12345
# 654321
# 1234567
n = 7
for i in range(1, n+1):
    if i % 2 == 0:
        numbers = list(range(i, 0, -1))
    else:
        numbers = list(range(1, i+1))
    print("".join(str(x) for x in numbers))

#2.
d1 = {"a": 1, "b": 2}  #out: a1,b2,b3,b4
d2 = {"c": 3, "d": 4}
output_list = [key + str(d1[key]) for key in d1] + [key + str(d2[key]) for key in d2]
output = ",".join(output_list)
print(output)

#3.
inp = "  ab  cd 12  "   #out = "abcd12"
# Using by method:
print(inp.replace(" ", ""))
# Using without standard method :
out = ""
for c in inp:
    if c.strip():
        out += c

print(out)