# Get a student data which has Name, Roll no and Marks WAP code to sort it in Ascending order
students = [
    ("Naveen", 101, 85),
    ("Dinesh", 102, 75),
    ("Ankit", 103, 92)
]
students.sort(key= lambda x: x[2])
print(f"Name\tRoll No\tMarks")
for student in students:
    print(student[0], "\t", student[1], "\t", student[2])

# Write a polymorphism method overriding concept example code:
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
