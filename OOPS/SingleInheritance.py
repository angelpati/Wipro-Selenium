#parent- child class , properties form parent class are acquired to child class

#parent class

class Employee:
    def __init__(self,name,empid):
        self.name=name
        self.empid=empid

    def empdetails(self):
        print(self.name,self.empid)
#child class
class Manager(Employee):
    def approve_leave(selfself):
        print("leave approved")
m = Manager("Angel",2021473184)
m.empdetails() #from parent class
m.approve_leave() #from child class

