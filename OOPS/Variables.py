#variable are used to store data
#instace variables- global variables at class level
#local variable - inside the method only

#instance variables example
class Student:

    #class variables
    school="St Joseph Convent"

    def __init__ (self,name,marks):
        self.name=name   #instance variables or global variables
        self.marks=marks #instance variables or global variables

    def show(self):
        schoolcity="Banglore" #local variable -scope is inside the method
        print(self.marks, self.name)
        print(schoolcity)
        print(self.school)
s1 = Student("Angel",90)
s2 = Student("Anjali",80)

s1.show()
s2.show()

