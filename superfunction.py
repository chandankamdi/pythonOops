class Parent:
    def __init__(self,name):
        print("Parent __init__",name)

class Parent2:
    def __init__(self,name):
        print("Parent2 __init__",name)

class Child(Parent,Parent2):
    def __init__(self):
        print("Child __init__")
        #Parent.__init__(self,"Chandan")     #without using super
        super().__init__("Chandan")          #with using super. No need to write self

class Child2(Parent2,Parent):                  #by changing position of classes within brackets, super function will first call Parent2 then Parent
    def __init__(self):
        print("Child __init__")
        #Parent.__init__(self,"Chandan")     
        super().__init__("Chandan")          
        Parent.__init__(self, "Shubham")
        
child_obj=Child()

print(Child.__mro__)                 #method resolution order. Prints step by step resolution of  class or function 

child_obj2=Child2()                  