#NumPy indexing is used to acess or modify elements in an array
import numpy as np
a=np.arange(10)
print(a)
b=a[6]
print(b)

scores=['86','98','100','65','75']
arr=np.array(scores)

arr2=np.array([[1,2,3],[4,5,6]])
print(arr2[0,1])

arr=np.array([10,20,30,40,50])
print(arr[1:4])

#slicing
arr=np.array([0,1,2,3,4,5,6,7,8,9])
print(arr[1:8:2])

arr=np.arange(10)
s=slice(1,8,2)
print(arr[s])

#slice with starting parameter
arr=np.arange(10)
print(a[2:])
#slicing with stop parameter
arr=np.arange(10)
print(a[:7])
#using step paramter
a=np.arange(10)
print(a[::2])

#slicing of 2arrays
employees=np.array([
    [1,25,5000],
    [2,35,6000],
    [3,45,7000],
    [4,55,8000],
])
print("Information on employee 2:", employees[1])
print("Ages of employees from index 2 onwards",employees[2:,1])

arr_3d=np.arange(24).reshape(2,3,4)
print("Original 3d array:\n",arr_3d)
subarray=arr_3d[0,:,:2]
print(subarray)

#negative slicing
marks=np.array([93,87,98,89,67,54,32,21])
print(marks[-3:])


