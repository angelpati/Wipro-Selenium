#multiple inheritance is 2 parents and one child class

class Parent1:
    pass

class Parent2:
    pass

class child(Parent1,Parent2):
    pass



#real life example

class Father:
    def driving(self):
        print("Father has the skill to drive")
class Mother:
    def cooking(self):
        print("My mother has a skill to make the most delicious food in this world")

class me(Father,Mother):
    def bothskilss(self):
        print("I have a skills to be very talkative")
        print("I know both the skills hihihi")


c=me()
c.driving()
c.cooking()
c.bothskilss()