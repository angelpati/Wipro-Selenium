'''
    Using numpy.array() Function
    Using numpy.zeros() Function
    Using numpy.ones() Function
    Using numpy.arange() Function
    Using numpy.linspace() Function
    Using numpy.random.rand() Function
    Using numpy.empty() Function
    Using numpy.full() Function
'''

#1D ARRAY
#This function creates a NumPy array filled with zeros
#By default, the data type is float64
import numpy as np
from numpy.ma.core import identity

a=np.zeros(5)
print(a)
#2D arrays of zeros
a_2D=np.zeros((4,3))
print(a_2D)

#Using numpy.ones() Function
a=np.ones(5)
print(a)

#2D array of ones
a_2D= np.ones((4,3))
print(a_2D)

#using numpy.arange() Function
#The numpy.arrange() function creates an array by generating a sequence of numbers based on the
#It is similar to the Python's bulit-in range() function.

a=np.linspace(0,10,num=5,endpoint=True)
print(a)

#exclude the last number
a=np.linspace(0,10,num=5,endpoint=False)
print(a)



#Using numpy.random.rand() Function
#generates an array of the specified shape with randon values in between 0 and 1
#If no argument is provided, it returns a single random float value

a=np.random.rand(5)
print(a)

#2D
a=np.random.rand(2,3)
print(a)

#3D
a=np.random.rand(2,3,4)
print(a)

#using numpy.empty() Function
#2D
#This function initializes an array without initializing its elemnets
#the content of the array is arbitary and may vary

a=np.empty((2,3))
print(a)

#uding numpy.full() fincation
#in the following example, we are using


#numpy.eye()
#the numpy eye() function is used to
#create a 2D array with ones on the diagonal and zeros in all other positions

identity_matrix=np.eye(4)
print(identity_matrix)

#numpy.diag
#in case of 2D array, the function extracts the dialgonal elements
#in case of 1D array, the function creates a square daigonal matrix
#the diagonal values are zeros in remaining positions.

Matrix=np.array(([[10,20,30],[40,50,60],[70,80,90]]))
print("Original matrix",Matrix)
Diagonal_elements=np.diag(Matrix)
print("Daigonal elements",Diagonal_elements)









