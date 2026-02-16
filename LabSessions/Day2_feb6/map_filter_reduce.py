#From a list of numbers: Filter even numbers Square them Find their sum
from functools import reduce
nums = [1, 2, 3, 4, 5, 6]
print(lambda x: x%2==0,nums)
print(reduce(lambda x,y: x+y,nums))
print(reduce(lambda x,y: x*y,nums))
sq=(list(map(lambda x: x*x, nums)))
print(sq)


salaries = [25000, 40000, 32000, 18000]
print(list(map(lambda x: x>30000,salaries)))
hiked_salaries = list(map(lambda s: s + (s * 0.1), salaries))
print("salaries after hike:")
print(hiked_salaries)

total_payout = reduce(lambda x, y: x + y, hiked_salaries)
print("total payout:",total_payout)








