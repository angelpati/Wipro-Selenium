#write a program to handle invalid user input
try:
    num=int(input("enter a number"))
    print(num)
except :
    raise ValueError("Invalid user Input")

#Write a Python program that generates random alphabetical characters, alphabetical strings, and alphabetical strings of a fixed length. Use random.choice()