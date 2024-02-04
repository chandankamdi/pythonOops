import square
from triangle import Triangle

s1=square.Square()             #depending on import we can write like this or like next method
s1.setvalues(40,20)
s1.setcolor("Green")
print(s1.area(),s1.getcolor())

s2=Triangle()
s2.setvalues(40,20)
s2.setcolor("Red")
print(s2.area(),s2.getcolor())