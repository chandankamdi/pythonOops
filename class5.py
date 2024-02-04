class Polygon:
    __width=None
    __height=None
    
    def set_values(self,height,width):      
        self.__width=width
        self.__height=height
        
    def get_height(self):
        return(self.__height)
    
    def get_width(self):
        return(self.__width)
    
class Square(Polygon):     #read as a relation: Square is a Polygon  or  Square is a derived class class of polygon
    def area(self):
        return self.get_height()*self.get_width()
    
class Triangle(Polygon):
    def area(self):
        return 0.5*self.get_height()*self.get_width()
    
s1=Square()
s1.set_values(40,20)
print(s1.area())

s2=Triangle()
s2.set_values(40,20)
print(s2.area())