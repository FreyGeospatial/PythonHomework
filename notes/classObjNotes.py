# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 13:34:27 2019

@author: JFrey
"""

#creating classes:
class Point:
    pass

#assign class to object
p1 = Point()
type(p1)
print(p1) #Creating a new object is called instantiation, 
            #and the object is an instance of the class,
            


#define attributes
p1.x = 100.0
p1.y = 200.0

p2 =  Point()
p2.x = 100
p2.y = 200

#both are point objects, but even though they contain same attributes,
#they are still different objects
p1 == p2

#however, we can check to see that the attributes are equal (or not)
p1.x == p2.x



class Rectangle():
    pass

#objects within objects
box = Rectangle()
box.width = 100.0
box.height = 200.0
box.llcorner = Point()
box.llcorner.x = 0.0
box.llcorner.y = 0.0



#adjust casing
myString = "blah"
print(myString.upper())


myDict = {"blah1":1, "blah2":2, "blah3":3}
type(myDict)
myDict["blah1"]
myDict.items() #object of class dict_items
type(myDict.items())


#the first parameter of any method is called 'self',
#which tells the object to act on itself, rather than on another object









