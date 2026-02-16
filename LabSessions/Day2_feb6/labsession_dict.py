#1
my_dict={1:"Angel",
         2:"Akansha",
         3:"Anjali"}
print(my_dict)

#Access the value of a key that exists and one that does not exist
my_dict2={1:"Angel",
         2:"Akansha",
         3:"Anjali"}
print(my_dict2[1]) #acessing the value of key
#Update the value of an existing key in a dictionary.
my_dict3={1:"Angel",
         2:"Akansha",
         3:"Anjali"}


my_dict3={1:"Angel", #updating the value
         2:"Unmisha",
         3:"Anjali"}
print(my_dict3)
#Delete a key from a dictionary using:
#del
#pop()
my_dict4={1:"Angel",
         2:"Unmisha",
         3:"Anjali"}
del my_dict4[1]
print(my_dict4)
my_dict4.pop(2)
print(my_dict4)
#Find the number of key–value pairs in a dictionary.
my_dict5={1:"Angel",
         2:"Unmisha",
         3:"Anjali"}
count=len(my_dict5)
print(count)
#Print only:
#keys
#values
#key–value pairs
my_dict6={1:"Angel",
         2:"Unmisha",
         3:"Anjali"}
for keys in my_dict6.values():
    print(keys)

for values in my_dict6.values()
    print(values)
for keys,values in my_dict6.items():
    print(keys.values)

