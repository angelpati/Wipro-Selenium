#create a student_id set integer type
stu_id={112,113,114,115}
print(stu_id)

#create a string type set
stu_id2={'a','b','c','d','e',113,115}
print(stu_id)

#create a mixed set
mixed_set={"Hello", 1, -7,8,9}
print(mixed_set)

#create an empty set
#empty_set =set()

#add elements to set
stu_id.add(1007) #will add in the starting
print(stu_id)
x=stu_id.copy()
print (x)
a=stu_id.difference(stu_id2)# it will return id 1 set
print (a)
b=stu_id2.difference(stu_id) #it will return id2 set
print (b)
stu_id.difference_update(stu_id2)#it removes the items which is in both the sets
print (stu_id)
stu_id.discard(112)# it will remove a particular item
print(stu_id)
fruit={"apple", "banana", "kiwi"}
vegetable={"apple", "carrot", "potato"}
inter=fruit.intersection(vegetable) #it will return the common item prest in both the sets
print("intersection", inter)
fruit.intersection_update(vegetable)
print("intersection update",fruit )
disjoint=fruit.isdisjoint(vegetable)
print(disjoint) #returns True if none of the items are present in both sets, otherwise it returns False.

















