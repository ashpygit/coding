from array import *

#-----------------------------XXXX-------------------------

five_val_arr = array('i',[9,8,7,6,2])

new_arr = array(five_val_arr.typecode, [])

for i in range(len(five_val_arr)):
    if i==2:
        continue
    else:
        new_arr.append(five_val_arr[i])

arr_len = len(five_val_arr)

print(arr_len)
print("five value of array is: ",five_val_arr)

arrList = []

for i in range(arr_len):
    arrList.append(five_val_arr[arr_len-1])
    arr_len -= 1

five_val_arr=('i',arrList)

print("Reversed Array is ",five_val_arr)

