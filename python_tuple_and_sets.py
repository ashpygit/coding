tup=(1,2,3,2,4,5,2,2)

print("This is tuple: ",tup)

#Tuple is immutable, see
print(tup[1])
#tup[1] = 99  #Show Error, Can't assign a value to tuple.
#print(tup)

print(tup.count(2))
print(len(tup))

'''########################################## SET #################################################### '''


sets={1,2,3,4,3,2,7,8,3}    

print("This is a sets: ",sets)

#print(sets[1]) --> No Indexing because set is collection of unique, unordered items
#sets_abc={[1,2,3,4],[1,2]} --> Sets can contain only immutable items - numbers,string,tuple (not list or dictionaries)

'''
Tuples are immutable, so they can be used as set elements.

Useful when you need to store unique records of multiple values.

Set makes sure that no duplicate tuple exists.
'''