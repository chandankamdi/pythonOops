#first letter of class name should be capital letter

class Student:
    def __init__(self):
        self.name="Chandan"
        self.age=28
        self.marks=95
    
    def talk(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Marks: ",self.marks)

s1=Student()

print(s1.name)
s1.talk()
s1.name="Kamdi"
print(s1.name)

s2=Student()
print(s2.name)