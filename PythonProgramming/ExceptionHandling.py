#exceptions- runtime errors which will disrupt the normal program flow
#benefits
#helps in debugging
#prevents program crashing
#handling errors and exceptions in the code



#try except

#try-code to be executed
#except- exception details catching
#else: if the exception does not occur then else part will get executed
#finally-mandated code
#custon exceptions

try:
    a=int (input("Enter the number"))
    b= int (input("Enter the number"))
    print(a/b)
except ZeroDivisionError:
    print("Cannot divided by zero")
except ValueError:
    print("Please enter valid numbers2")


#generic exception
try:
    a=5/10
except Exception as e:
    print(e)
#runs only if there is no exception
else:
    print("Division Successful")
finally:
    print("Close the Bowser now")

#custom exceptions- creating a own exception
age= int(input("Enter the age"))
if age<18:
    raise ValueError("Age must be above 18 or above")






