"""1.Take input from the user(name, age, marks)
2. Create a class with __init__ method and also create a action method diplay() to print attributes
3.Also try to use Arguments and Parameters with different objects
    """

x=input("Enter your name: ")
y=int(input("Enter your age: "))
z=int(input("Enter your marks: "))

class Student:
    def __init__(self,x,y,z):       #once the class is called; the init will initialize. all other function needs to be called as per requirement
        self.name=x                 #init is constructor. only once it can be given in a class. if we give more than once then last init will work.
        self.age=y
        self.marks=z
    
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Marks: ",self.marks)

s1=Student(x,y,z)      

s1.display()