#Create a class Book with attributes title and author. create 3 different book objects and print all details
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print(self.title)
        print(self.author)
book1=Book("Maths","RD Sharma")
book2=Book("ThePearsons","Pearson")
book3=Book("Springer","The Brothers")
book1.display()
book2.display()
book3.display()

#Create a class Rectangle with a constructor that takes length and width and stores area and perimeter as object attributes.
class Rectangle:
    def __init__(self,length,width):
        print("I am the rectangle constructor")
        self.length=length
        self.width=width
        self.area=length*length
        self.paramter=2*(length+width)
rectan=Rectangle(40,20)
print(rectan.area)
print(rectan.paramter )


