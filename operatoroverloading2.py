class Python:
    def __init__(self,pages):
        self.pages=pages               #b1.__add__(b2) means add method comes under b1 object. so we heve to add add function in this class only

    def __add__(self,other):
        return self.pages+other.pages
class Java:
    def __init__(self,pages):
        self.pages=pages

b1=Python(300)
b2=Java(400)

print(b1+b2)
#print(b2+b1)       #this will give error as now add function should be under b2