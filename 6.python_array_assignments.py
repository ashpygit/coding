from array import *

'''
Create an array with 5 values and delete the value at index number 2 without using in-built function.
'''
user_arr=array('i',[])

arr_size=int(input("Enter the size of the array: "))

for i in range(arr_size):
    arr_vals=int(input("Enter the value of the array: "))
    user_arr.append(arr_vals)

print(user_arr)

get_index_val=int(input("Which Index position value you wants to delete: "))

user_arr.pop(get_index_val) #or del user_arr[get_index_val]

print("Value deleted at index position ",get_index_val,"--->", user_arr)