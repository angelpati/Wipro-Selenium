#operator polymorphism means
#the same operator behaves differently for diff data types or the objects
# add numbers
#+join the strings
# +merges the lists
#operator overloading in python

#python
'''
__add__()
__sub__()
__mul__()
__eq__()
'''

class Number:
    def __init__(self,value):
        self.value=value
    def __add__(self, other):
        return self.value+other.value
n1=Number(10)
n2=Number(20)
print("Addition")
print(n1+n2)
#now + will work for the custom objects
class Number:
    def __init__(self,value):
        self.value=value
    def __mul__(self, other):
        return self.value*other.value
n1=Number(10)
n2=Number(20)
print("Multiplication")
print(n1*n2)
#greater number program
class Number:
    def __init__(self,value):
        self.value=value
    def greater(self, other):
        if self.value>other.value:
            return self.value
        else:
            return other.value
n1=Number(10)
n2=Number(20)
print("greater number is ")

print (n1.greater(n2))