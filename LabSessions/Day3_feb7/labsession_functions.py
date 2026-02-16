#.Write a Python function to sum all the numbers in a list.
def sumofall(num):
    sum=0
    for n in num:
        sum=sum+n
    return sum
print(sumofall([1,2,3,4,5]))
#Write a Python function to find the maximum of three numbers.
def max(num1,num2,num3):
    if num1>num2>num3:
        return num1
    elif num2>num3:
        return num2
    else:
        return num3
print("maximum")
print(max(23,36,46))