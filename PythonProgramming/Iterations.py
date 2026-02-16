#using list
a=[10,20,30,40]
itera=iter(a)
print(next(itera))
print(next(itera))
print(next(itera))
print(next(itera))

#using string
a=("Hello")
itera=iter(a)
print(next(itera))
print(next(itera))
print(next(itera))
print(next(itera))

#uding dictionary
d={'a':1,'b':2,'c':3}
itera=iter(d)
print(next(itera))
print(next(itera))
print(next(itera))

#uding for loop
for key in itera:
    print(key)
d={'a':1,'b':2,'c':3}
for key,value in d.items():
    print(key,">",value)

#iter(callablr, semtinel)
def get_input():
    return input("enter the nuumber")
for value in iter(get_input,quit):
    print("you enterred",value)
print("loop ended")

