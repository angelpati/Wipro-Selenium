#function is a block of code that performs a specific task
#def functionname()

def printdata():
    print("Hello World")
#call the function
printdata()

def printdata(a,b):
    print(a+b)
#call the function
printdata(3,4)

#function with parameters
def printdata(name):
    print("hello",name)
#pass the argument
printdata("Angel")


#return statement
#to return the function value return statement is used
def sq(num):
    result=num*num
    return result
#function call
square=sq(3)
print("square",sq)
#my method
print(sq(4))

#function pass
def func_pass():
    pass
#call the function here
func_pass()

#multiple return values
def cal(a,b):
    return a-b, a+b,a*b
add, sub, mul =cal(10,5)
print(add)
print(sub)
print(mul)

#function calling another function
def areaofret(len,wid):
    return len*wid
def areraofsq(side):
    return side*side
value =(areaofret(4,6))
print(areraofsq(value))

#mam method
sq=areraofsq(value)
print(sq)


#function with a loop
def even(limit):
    for i in range(2,limit +1,2):
        print(i)
even(10)

def even(limit):
    if limit%2==0:
        return "even"
    else:
        return "odd"
print(even(10))
print(even(11))
