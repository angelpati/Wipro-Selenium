'''''
Method Overriding with Inheritance
Create a base class Employee with a method calculate_salary().
Create a subclass Manager that overrides calculate_salary() and adds a bonus.
Demonstrate runtime polymorphism using parent class reference.

'''



class Employee:
    def __init__(self,salary):
        self.salary=salary
    def calculate_salary(self):
        return self.salary
class Manager(Employee):
    def __init__(self, salary,bonus):
        super().__init__(salary)
        self.bonus=bonus
    def calculate_salary(self):
        return self.salary+self.bonus

b=Manager(10000,345)
print(b.calculate_salary())

#Polymorphism Using Function Arguments
'''
Create classes Dog, Cat, and Cow each with a method speak().
Write a function animal_sound(obj) that calls speak().
Pass different objects to the same function.
'''
class Dog:
    def speak(self):
        print("Dog bark")
class Cat:
    def speak(self):
        print("Cat meow")
class Cow:
    def speak(self):
        print("Cow")
def animal_sound(obj):
    obj.speak()

animal_sound(Dog())
animal_sound(Cat())
animal_sound(Cow())

'''
Multilevel Inheritance with Polymorphism
Create Vehicle → Car → ElectricCar.
Each class overrides the method fuel_type().
Call the method using different object references.
 '''
class Vehicle:
    def fuel_type(self):
        print("dont know")
class Car(Vehicle):
    def fuel_type(self):
        print("Petrol")
class ElectricCar(Car):
    def fuel_type(self):
        print("Electric")
def Cars(car):
    car.fuel_type()
v=Vehicle()
c=Car()
e=ElectricCar()
Cars(v)
Cars(c)
Cars(e)


'''
Operator Overloading
Create a class BankAccount with attribute balance.
Overload + to add balances and > to compare balances.
Demonstrate polymorphic behavior of operators.
'''
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def addbal(self,adbal):
        self.adbal=adbal
    def compare(self):
        if




