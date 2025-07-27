from numpy import *

arr1 = array([1,2,3,4.5,5,6,7,8])
print(arr1.dtype)
print(arr1)

arr2 = linspace(0,5,4)
print(arr2)

arr3 = linspace(0,5)
print(arr3)

arr4 = array([[1,2,3,4.5],[5,6,7,8]],int)
print(arr4.dtype)
print(arr4)

arr5 = arange(1,21,4)
print(arr5)

arr6 = logspace(1,40,4)
print(arr6)
print('%.2f' %arr6[3])

arr7 = zeros(5,int)
print(arr7)

arr8 = ones(10,int)
print(arr8)