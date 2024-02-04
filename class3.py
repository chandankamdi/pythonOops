#private attribute


class Speed:
    def __init__(self):
        self.speed=10
        self.__newspeed=80               #two undeerscores before attribute means this is private.
        
    def getnewspeed(self):               #getter: get value
        return self.__newspeed
    
    def setnewspeed(self,m):             #setter: set value
        self.__newspeed=m

s1=Speed()
print(s1.speed)

#print(s1.__newspeed)                    #we cannot access directly access attribute with prefix __ 
print(s1.getnewspeed())                  #we have to use additional function to access it

s1.__newspeed=90                        #but we can modify it directly
print(s1.__newspeed)                    #once modified we can access it

#Using getter and setter
s2=Speed()
print(s2.getnewspeed())
s2.setnewspeed(30)
print(s2.getnewspeed())

