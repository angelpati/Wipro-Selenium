

#we can parametrized the constructors
#self is mandatory
#syntax __init__



class Student:
    def __init__(self):
        print("Constructor is called")

    def addsum(self):
        print("Adding two numbers")
s1=Student()
s1.addsum()

#parametrized constructors
#self.name is a instance variableor a global variable(belongs to the object)
#name is a local parameter(exists inside the method)
#if we dont assign it to the self.namethe object will not remember the value


class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary= salary
    def display(self):
        print(self.name, self.salary)

e1 = Employee("Angel",38494)
e2=Employee("Anjali",38494)
e1.display()
e2.display()


#constructor overloading is not supported so that we have to use paramatrized one

#using * args in constructor
#constructor overloading is supported by * args
# we can pass any number of paramters to the constructor using * args

class Numbers:
    def __init__(self,* args):
        self.values=args
n=Numbers(10,20,30)
print(n.values)

m = Numbers(3,4)
print(m.values)

p=Numbers(3)
print(p.values)

#Parent and child constructors
#super keyword for acessing parameters

class Parent:
    def __init__(self):
        print("I am the parent constructor")
class Child(Parent):
    def __init__(self):
        super().__init__() #for calling parent constructor
        print("I am the child constructor")
c=Child()











