from polygon1 import Polygon
from shape import Shape

class Triangle(Polygon,Shape):
    def area(self):
        return 0.5*self.getheight()*self.getwidth()