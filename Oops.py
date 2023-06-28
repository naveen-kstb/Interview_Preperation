print("This is OOOPS Concept Multiple Inheritance")


class version1:
    def build1_1(self):
        a = 10
        b = 20
        print(a + b)

    def build1_2(self, a, b):
        print(a - b)


class version2:
    def build2_1(self):
        a = 5
        b = 2
        print(a * b)


class version3(version1, version2):
    def build3_1(self, a, b):
        print(a / b)

    def build3_2(self, x, y):
        print(x ** y)


a = version3()
a.build3_1(10, 5)
print(type(a.build3_1))
a.build2_1()
a.build1_2(20, 10)
a.build3_2(2, 3)

