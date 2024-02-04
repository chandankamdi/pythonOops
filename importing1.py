#importing built in and user defined modules(python file)

import math   #built in module

import mymath  #importing our file mymath. since both are in same directory we write like this

print(mymath.sum(20,30))


from sample import mymathnew   #importing file when it is in another folder
print(mymathnew.divide(40,20))


import sample.mymathnew
print(sample.mymathnew.divide(100,25))

import sample.mymathnew as newfunc     #giving new name to our module
print(newfunc.divide(150,25))
