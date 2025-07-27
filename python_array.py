from array import *

vals = array('i',[10,8,6,4,2])

print(vals)
print(vals.typecode)
print(vals.buffer_info())
print(len(vals))

print("-----X-----")


for val in vals:
    print(val)


print("-----X-----")

i=0
while i<len(vals):
    print(vals[i])
    i+=1

print("-----X-----")

firstArr = array('u',['a','c','x','b','y','z'])
print(firstArr)
print("value of index 2 is ",firstArr.index(2))

secondArr = array(firstArr.typecode,sorted(firstArr))
print(secondArr)

for e in secondArr:
    print(e)