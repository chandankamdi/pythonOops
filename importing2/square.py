import polygon1
import shape

class Square(polygon1.Polygon,shape.Shape):
    def area(self):
        return self.getheight()*self.getwidth()
    
    