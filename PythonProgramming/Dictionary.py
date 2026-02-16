county={"India" :"Delhi" ,
        "Canada" : "ottawa"}
print (county)
#acess the value with keys
print(county["Canada"])
#add elemnts
county["Italy"]="Rome"
print (county)
#rem elements
del county["India"]
print (county)
#iterate among the dict
#for coun in country:
    #print("coun",coun)

#integer as a key

my_dict= {1:"one", 2:"two", 3:"three"}
print(my_dict)
my_dict= {1:"one", 2:"two", 3:"three",1:"four"}
print(my_dict)

#tuples as a key
my_dict ={(1,2):"one two", (3):"three"}
print(my_dict)

my_dict={(1,2):"one two",(3):"four"}
print(my_dict)
value = my_dict.pop((1, 2))
print(value)     # 'one two'
print(my_dict)

#list as key
#my_dict={1 :"Hello", [1 , 2]:"There you"}
#print(my_dict)
employess=[{"id":1, "name":"Angel","Role":"seniour Developer"}]
print(employess[0])
print(employess[0]["name"])
for emp in employess:
    print(emp["name"], emp["Role"])

employess.append({"id":2,"name":"Akansha","Role":"Developer"})
print(employess)

#search item in the list
for emp in employess:
    if emp["name"] =="Angel":
        print(emp)
