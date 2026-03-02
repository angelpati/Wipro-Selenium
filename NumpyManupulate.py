import numpy as np
from pycparser.c_ast import ArrayDecl

#changing Shape

#reshape

a=np.arange(1,7)
print("Original array",a)
reshaped=a.reshape(2,3)
print(reshaped)

#flat= 1D iterator over the array

arr=np.array([[1,2],[3,4]])
for x in arr.flat:
    print(x)

#flatten- returns a copy of array collapsed into one dimentional

arr=np.array(([[1,2],[3,4]]))
print(arr)
at_arr=arr.flatten()
print(at_arr)
#ravel()- Returns a flattened array
arr=np.array([[1,2],[3,4]])
print(arr)
at_arr=arr.ravel()
print(at_arr)

#pad()- returns a padded array with shape increased accroding to pad_wodth.
arr=np.array([1,2,3])
padded=np.pad(arr,2,mode='constant')
print(padded)

''' Transpose operations
1   transpose
Permutes the dimensions of an array
2   ndarray.T
 as self.transpose()
3   rollaxis
Rolls the specified axis backwards
4   swapaxes
Interchanges the two axes of an array
5   moveaxis()
Move axes of an array to new positions
'''

#1  transpose
# reorders the dimensions of an array.
# rows will become the columns

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.transpose()
print(transpose)

#2 ndarray.T
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.T
print(transpose)

#rollaxis - Rolls the specified axis backwards

arr = np.zeros((2,3,4))
print(arr)

# 2 is the blocks - axis 0
# 3 - rows - axis 1
# 4 columns - axis 2

#(0,1 ,2) - (2,3,4)
#(2,0,1) - (4,2,3)

#arr[block][row][column]

new_arr = np.rollaxis(arr, 2)
print(new_arr)

#swapaxes() - Interchanges two axes of an array.
#$Axis 0 and Axis 2 swapped.
arr = np.zeros((2,3,4))
print(arr)

new_arr = np.swapaxes(arr, 0 , 2)
print(new_arr)
# (4 3, 2)

#moveaxis() - Moves specified axes to new positions.
arr = np.zeros((2,3,4))
print(arr)
new_arr = np.moveaxis(arr, 0, -1)
print(new_arr)

# (3 ,4 2)

#joining arrays
#concatenate()-joining 2 arrays

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])

print(np.stack((a,b),axis=0))
print(np.stack)

a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.stack((a,b),axis=0))
print(np.stack((a,b),axis=1))

#hstack- stacks arrays horizontally (column-wise)

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])

print(np.hstack((a,b)))
print(np.concatenate((a,b),axis=1))

#vstack()- stack arrays vertically
print(np.vstack((a,b)))
print((np.concatenate((a,b),axis=0)))

#column_stack()- stack 1D arrays as columns into 2D arrys
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.column_stack((a,b)))

#row stack
print(np.vstack((a,b)))

#SPITTING ARRAYS
#split arrays into multiple sub-arrays
arr=np.array([1,2,3,4,5,6])
result=np.split(arr,3)
print(result)

#work on 2D arrays

arr2=np.array([[1,2,3,4],[5,6,7,8]])
print(np.split(arr2,2))

#vsplit() Splits array vertically row-wise

arr2=np.array([[1,2],
               [3,4],
               [5,6],
               [7,8]])
print(np.vsplit(arr2,2))


#adding/Removing elements
#resize()-Returns a new array with a specific shape
ar=np.array([1,2,3,4])
new_arr=np.resize(arr,(2,3))
print(new_arr)

#the ements will repeat in the new array
#return a new array

#append()-Appends a value at the end of an array
arr=np.array([1,2,3])
new_arr=np.append(arr,[4,5])
print(new_arr)

#unique()
arr=np.array([1,2,3,4,5])
print(np.unique(arr))

#Repeating
#repeat() is used to repeat each element
arr=np.array([1,2,3])
print(np.repeat(arr,3))

#different repeats for each eleemt
arr=np.array([10,20,30])
print(np.repeat(arr,2,axis=0))

#tile()-the input array that will be repeated.

my_array=np.array([1,2,3])
titled_array=np.tile(my_array,2)
print("Original Array:",my_array)
print("Titled Array:",tilted_array)

#Rearranging Elements
#flip()- Reverses the order of elements along a given axis
#if axis=None- reverses entire flattened array
#if axis=0 - reverse rows
#if axis=1- reverse columns

arr=np.array([1,2,3,4])
print(np.flip(arr))
#2D
arr2=np.array([[1,2],
               [3,4]])
print(np.flip(arr2,axis=0))

print(np.flip(arr2,axis=1))

#fliplr() - FLIP LEFT-RIGHT (axis=1)- Works only on 2D + arrays.
arr2=np.array([[1,2,3],
               [4,5,6]])
print(np.fliplr(arr2))

#flipud- Flip Up-Down(axis=0)
print(np.flipud(arr2))

#roll() -Rolls(rotates) elemts along a given axis.
arr2= np.array([[1,2,3],
                [4,5,6]])
np.roll(arr2,2,axis=None)
#Sorting n Searching
#sort() returns a sorted copy of an array(or sorts in-place if using ndarray method).
arr=np.array([5,2,9,1])
sorted_arr=np.sort(arr)
print(sorted_arr)

#argsort()- Returns the indices that would sort the array return the index positions
arr=np.array([5,2,9,1])
sorted_arr=np.sort(arr)
print(sorted_arr)
indices=np.argsort(arr)
print(indices)

#lexsort- used for sorting with mutiple columns (like sorting by last name, then first name)
#sort by first
#then by b(secordary key)
#sorting happens from right to left
a=np.array([1,1,0,0])
b=np.array([1,0,1,0])
result=np.lexsort((b,a))
print(result)














