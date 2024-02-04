from abc import ABC, abstractclassmethod
from abc import *                    #imports all the classes present in abc. bad for memory. slows the import process


class Shape(ABC):
    @abstractclassmethod
    def area(self):
        pass
    
    @abstractclassmethod
    def perimeter(self):
        pass
    
class Square(Shape):
    def __init__(self,side):
        self.__side=side
        
    def area(self):
        return self.__side*self.__side
    
    def perimeter(self):
        return 4*self.__side
        
#triangle_obj=Shape()       #if we want that our class should not be assigned to any attribute then we can use abstractmethod by importing abstract
                            #it we throw an error    
    
square_obj=Square(10)
print(square_obj.area())