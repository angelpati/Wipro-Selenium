#Write a Python function to check whether a number falls within a given range.
a=range(1,10)
num=int(input("enter the number"))
for i in a:
    if(num==i):
        print("the number falls under the range")
        break
else:
        print("out of range")