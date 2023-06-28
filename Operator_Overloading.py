# Types of operator overloading is __add__, __sub__, __mul__, __truediv__

class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, obj2):
        print("Name:", self.name)
        return self.salary * obj2.days


class payroll():
    def __init__(self, days):
        self.days = days


obj1 = Employee('Naveen', 2000)
obj2 = payroll(28)
print("Net Salary:", obj1 * obj2)
