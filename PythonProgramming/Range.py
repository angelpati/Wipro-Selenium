a= range(5)
print(a[1])
print(a[3])
a=range(2,5)
for i in a:
    print (i)
a=range(2,5,3)
for i in a:
    print (i)
a=range(2,20,-3)
for i in a:
    print(i)
a=range(15,2,-1)
for i in a:
    print(i)
for attempt in range(3):
    pin=input("enter the pin")
    if pin=="1234":
        print("Login sucessful")
        break
    else:
        print("Acoount Locked")