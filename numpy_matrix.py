from numpy import *

arr = array([1,2,3,4,5,6])

print(arr.reshape(2,3))
print(arr.ndim)


arr1 = array([[1,2,3,4,5],[1,2,3,4,5]])

print(arr1)
print(arr1.ndim)
print(arr1.flatten())

m = matrix(arr1)
m1 = matrix(arr)

print(m.diagonal())
print("Minimum value in array in matrix m: ",m.min())
print("Max value in array in matrix m1: ",m1.max())