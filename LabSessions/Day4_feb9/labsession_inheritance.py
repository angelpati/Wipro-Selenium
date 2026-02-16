#cerate a python program with class name savingsccount and functions deposit in parent class  and  addinterest in the child class
class Savingaccount:
    def __init__(self,balance):
        self.balance= balance
        print("This is your balance")
    def deposit(self,amount):

        if(amount>0):
            self.balance+=amount
            print("This is your savings")
        else:
            print("Invalid")
class Intrest(Savingaccount):
    def addintrest(self,rate):
        addintrest=self.balance*rate/100
        self.balance+=addintrest
        print("This is your intrest")
a=Intrest(10070095)
print(a.deposit(500))
print(a.addintrest(10))
print(a.balance)





