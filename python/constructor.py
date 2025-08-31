"""__init__ our constructor"""

#without constructor

class car:
    def set_details(self, brand, color):
        self.brand = brand
        self.color = color

#creating obj
car1 = car()
car1.set_details('tesla','red')

print(car1.brand)
print(car1.color)

#with constructor
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car('tesla','red')#values automatically set
print(car1.brand, car1.color)        

"""
syantax:
class classname:
   def __init__(self,parameters1, parameters2)
        self.property1 = parameters1
        self.property2 = parameters2

__init__() act as a constructor
self.proprety store the value        
"""
# one more example

class student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

student1 = student('mithoon',100,'A+')
student2 = student('jaggu',50,'B+')

print(student1.name,student1.age, student1.grade)
print(student2.name,student2.age, student2.grade)

"""
1- default constructor
2- parameterized constructor (self, name, age)
3- constructor with default values, (self, name="unkown",age=0)
"""
