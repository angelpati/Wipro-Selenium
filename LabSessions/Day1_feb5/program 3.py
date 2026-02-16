#Print all numbers divisible by 5 between 1 and 100
a= range(1,100)
for i in a:
    if i%5 ==0:
        print("even no from 1,50 is ", i)
# Create a list of numbers from 50 to 100 with a step of 5
a= range(50,100,5)
for i in a:
    print (i)
#fromr ange 1,10 sqaure of each number
a= range(1,11)
for i in a:
    print(i*i)
#Print numbers between -10 and 10.
a=range(-10,11,1)
for i in a:
    print (i)
#Write a Python function to Sum of numbers from 1 to 100
a=range(1,101)
sum=0
for i in a:
    sum=sum+i
print("sum is",sum)