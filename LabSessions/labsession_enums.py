#What is the output?

#list(enumerate(['a', 'b', 'c']))
list=['a','b','c']
for i  in enumerate(list):
    print(i)



#Q2What is the output?

for i, v in enumerate([10, 20, 30]):
    print(i, v)
# 0 10, 1 20 , 2 30

#Write code to print index + value from:

colors = ['red', 'green', 'blue']
for val, color in enumerate(colors, start=1):
    print(val,color)
# What is the output?

#list(enumerate("PYTHON", start=1))
list=("PYTHON")
for ch,lists in enumerate(list):
    print(ch,lists)
# Find the index of value 50 using enumerate():

# nums = [10, 20, 30, 40, 50, 60]
nums = [10, 20, 30, 40, 50, 60]
for index , val in enumerate(nums):
    if val==50:
        print (index)
#What is the output?

for i, n in enumerate(range(10, 60, 10)):
    print(i, n)
#Convert this into an enumerate() loop:
data =[10,20,30]
for i , datas in enumerate(data):
    print(i,datas)

#for i in range(len(data)):
    #print(i, data[i])
#What is printed?

items = ['a', 'b', 'c']
for i in enumerate(items):
    print(i)
# What is the output?

#list(enumerate([], start=5))
list=["angel","24","2003"]
for i ,lists in enumerate(list, start=5):
    print(i,lists)
#What is the output?

for i, v in enumerate([100, 200, 300], start=-1):
    print(i, v)
#What happens here?

# i, v = enumerate(['x', 'y', 'z']) two values are there either only i or v
#Explain the difference:

enumerate(data) # starts from 0
enumerate(data, start=1)# srats from 1


