empty_list=[]
numbers=[1,2,3,4,5,6,7,8]
mixed_data=[1,"hello",True,6.67,1]
nested=[[1,2],[1,3]]

#acessing the list elements indexing concept
print(mixed_data[1])

#modifying the data
mixed_data[4]=6
print(mixed_data)

#add elements
mixed_data.insert(5,10) #it will insert 10 at the index of 5
print(mixed_data)

#append will add at the end
mixed_data.append("John")
print(mixed_data)

#remove elements
mixed_data.remove("John")
print(mixed_data)
mixed_data.pop() #pop the last element
print(mixed_data)
mixed_data.pop(1) #pop ny indexing
print(mixed_data)

#list methods
numbers.sort() #ascendingorder
print(numbers)
numbers.reverse() #reverse
print(numbers)
numbers.count(3)
print("count",numbers)
numbers.index(3)
print("index",numbers)
numbers.clear() #empty list

print (numbers)

fruits=["apple","banana","cherry"]
for item in fruits:
    print(item)
for i , fruit in enumerate(fruits):
    print(i,fruit)
#to get a particular portion from the list
my_list=['a','b','c','d','e','f']
print(my_list)
print(my_list[2:5])

#ommit start to end endices
print(my_list[5: ])

#from first item to last item
print(my_list[ : ])

#extends
numberss=[1,2,3]
numbersw=[4,5,6]
numberss.extend(numbersw)
print(numberss)

#to print largest number in the list
list=[10,40,29,89,300,58,800]
largest=list[0]
for n in list:
    if n>largest:
        largest=n
print("largest in the list",largest)
#to remove all even numbers from the list
list2=[22,44,35,56,78,97,57]
for  n in list2[:]:
    if n%2==0:
        list2.remove(n)

print(list2)
#multiply the items in list
list3=[1,2,3,4,5,6,7]
mul=1
for i in list3:
    mul=mul*i
print(mul)










