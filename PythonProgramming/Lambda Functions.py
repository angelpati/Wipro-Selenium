#to find even n odd
even= lambda a:a%2==0
print(even(3))

#to find maximum
max= lambda a,b: a if a >b else b
print(max(20,555))

#filter positive numbers
nums = [-5, 10, -3, 7, 0, 2]
positive=list(filter(lambda x: x>=0,nums))
print(positive)
#Filter non - empty strings
data = ["hello", "", "world", "", "python"]
non_empty=list(filter(lambda x : x!="", data))
print(non_empty)
#reduce
#aggregate-combining many values to one single result

from functools import reduce
nums=[10,20,30,40]
print(reduce(lambda x,y: x+y,nums))
print(reduce(lambda x,y: x*y,nums))
print(reduce(lambda x,y:x if x>y else y,nums))
print(reduce(lambda x,y:y if x>y else x,nums))

#map-transfroms the data-function is applied to every element
nums=[10,20,30,40]
sq=list(map(lambda x: x*x,nums))
print(sq)

data=[(1,3),(4,1),(2,2)]
sorteddata= sorted(data, key=lambda x: x[0])
print(sorteddata)

marks = {"A":75,"B":90,"C":60}
sortedmarks= dict(sorted(marks.items(), key=lambda x: x[1]))
print(sortedmarks)

nums = [1, 2, 3, 4]

print(list(map(lambda x: x % 2 == 0, nums)))

print(list(map(lambda x: x[0], ["python", "java", "c++"])))

nums = [1, 2, 3]

f = map(lambda x: x * 2, nums)

nums.append(4)

print(list(f))

print(list(filter(None, [0, "", None, 5, "Hi"])))




