#Private method or Private function

class Example:
    def __init__(self):
        self.x=10
        self._y=50
        self.__z=100
    
    def public_method(self):
        print(self.x)
        print(self._y)
        print(self.__z)
        self.__private_method()              #private function can be called in class but not in code+
    
    def __private_method(self):
        print("Inside private method")

s1=Example()
s1.public_method()
#s1.__private_method()        #Cannot call private function directly here. we have to call it in class only
