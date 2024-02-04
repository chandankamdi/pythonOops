a=10
b=20
print(a+b)         #here + acts as a addition

p="Hello"
q="World"
print(a+b)          #here + acts as a concatenation. This is called as polymorphism

x=[10,20,30]
y=[5,6,7]
print(x+y)

#+ is written with internal method as __add__ ie a+b = a.__add__(b)
class Books:
    def __init__(self,pages):
        self.pages=pages
        
    def __add__(self,other):
        return self.pages+other.pages
    
    def __mul__(self,other):
        return self.pages*other.pages
    
    def __gt__(self,other):
        return self.pages>other.pages
        
b1=Books(150)
b2=Books(100)

print(b1+b2)        #without __add__, here + will throw a error. we will have to manipulate existing quality of +. 
                    #after withing __add__ this will not give error
                    #b1.__add__(b2)
                    #similarly we will check for multiply and greather than operator
print(b1*b2)
print(b1>b2)