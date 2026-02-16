#class is a blueprint or a template
#which describes the state/ behaviour of its object
#data is put in variables
#behaviour is put in functions

class Student:
    #data or the properties
    studentname= "Angel"
    studentID= 2021473184

    #self is used to acces the attribute of the class we have defined
    #it is automatically loaded
    #self represents the instance of the class

#create a function to acess the data
    def deisplaysstudentdetails(self):
        print(self.studentname)
        print(self.studentID)


#create object of the class
a=Student()
a.deisplaysstudentdetails()


#write a program to create a class for emplyee id, name , adress, department. and create your function to display a data with two objects
class Employee:
    employee_name="Angel"
    employee_id=2021473184
    employee_address="Nandini Apartments"
    employee_department="Computer Science and Engineering"

def employeedetails(self):
    print(self.employee_name)
    print(self.employee_id)
    print(self.employee_address)
    print(self.employee_department)
a=Employee()
a.employeedetails()




