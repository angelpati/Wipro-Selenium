#poly morphism means taking many forms
#same method/ function name will behave differently depending on the object type
#input arguments
#class implementation


#object type
print(len("python"))
print(len([1,2,3]))
print(len({1,2,3}))

#imput arguments no of arguments/ data types

class Calculator:
    def add(self, a,b=0,c=0):
        return a+b+c
c=Calculator()
print(c.add(5))
print(c.add(5,10))
print(c.add(5,10,15))

#runtime polymorphism is supported
#achieved method overriding -child class method will override the parent class method
class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("dog barks")
a=Dog()
a.sound()