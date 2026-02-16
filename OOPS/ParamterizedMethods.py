
#default methods-bulit in methods, user defined meyhods- method name, method body
#parametrized methods it allow the same method to behave differently for diff inputs


#parametrized methods(multiple parameters)

class Calculator:
    def add(selfself,a,b):
        print(a+b)
c=Calculator()
c.add(10,20)
c.add(5,7)

#default parameters

class Test:
    def run(selfself,browser="chrome"):
        print("Running on",browser)
t=Test()
t.run()
t.run("firefox")



# *args parametrized methods

class Numbers:
    def total(selfself, *args):
        print(sum(args))
n=Numbers()
n.total(10,20,30)
n.total(10)
n.total(10,60)


