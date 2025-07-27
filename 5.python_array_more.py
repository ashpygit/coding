from array import *

vals=array('i',[])

arr_len=int(input("Enter the length of the array: "))

for i in range(arr_len):
    x = int(input("Enter the next value to store into array: "))
    vals.append(x)

print(vals)

xx=int(input("Now enter the Index in range of",arr_len," to search for the value"))

j=0
for e in range(arr_len):
    if xx==vals[e]:
        print("Value Index in Array is: ",j)
        break
    j += 1
    
