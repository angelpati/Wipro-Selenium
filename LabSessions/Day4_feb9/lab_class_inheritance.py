#Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter
from multiprocessing.util import sub_debug

from PythonProgramming.Function import areaofret


class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=3.14*self.radius*self.radius
    def perimeter(self):
        perimeter=2*3.14*self.radius
        print("radius of the circle",self.radius)
cir=Circle(10)
print("Area of the circle",cir.area())
print("Perimeter of the circle",cir.perimeter())

#Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age
from  datetime import date
class Person:
    def __init__(self,name,country,dob):
        self.name=name
        print("Enter the name",name)
        self.country=country
        print("Enter the country",country)
        self.dob=dob
        print("Enter the dob",dob)


    def calage(self):
        today = date.today()
        age = today.year - self.dob.year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1

        return age

p1 = Person("Angel", "India", date(2002, 5, 10))

print("Name:", p1.name)
print("Country:", p1.country)
print("Age:", p1.calage())



#Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
import math
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=math.pi*self.radius*self.radius
    def perimeter(self):
        perimeter=2*math.pi*self.radius

class Triangle(Shape):
    def __init__(self,base,height, side1,side2):
        self.base=base
        self.height=height
        self.side1=side1
        self.side2=side2
    def area(self):
        area=0.5*self.base*self.height
    def perimeter(self):
        perimeter= self.base+self.side1+self.side2
class Square():
    def __init__(self,side):
        self.side=side
    def area(self):
        area=self.side*self.side
    def perimter(self):
        perimeter=4*self.side


circle=10
triangle=10,12,24,24
square=24

print("area of the circle",circle.area())









#Write a python program to create a child class Bus that will inherit all of the variables and methods of the Vehicle class












#5.Write a python program to create  a Vehicle class without any variables and methods

