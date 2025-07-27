numbers=[12,56,34,87,56,43,22,12]
name=['black','Red','Orange','Apple']

print("Number List:",numbers)
print("Name List: ",name)
print("")

numbers.append(99) #Add 99 at the end of the list
print(numbers)
print(numbers[2:])
print("")

numbers.insert(3,55) #Insert 55 at 3rd Index Position
print(numbers)
print("")

numbers.remove(87) #remove number 87 from the list
print(numbers)
print("")

numbers.pop(1) #remove value at 1st Index position in the list.
print(numbers)
print("")

numbers.pop() #remove last value from the list.
print(numbers)
print("")

numbers.extend([1,2,4,5]) #Insert mutiple values in the list
print(numbers)
print("")


del numbers[8:] #delete mutiple value in the list.
print(numbers)
print("")

print("Max number in the list",max(numbers))
print("Min number in the list",min(numbers))
print("Sorting number in the list: ",numbers.sort(), numbers)

for i in sorted(numbers):
    print(i)

print("")

for i in sorted(numbers,reverse=True):
    print(i)