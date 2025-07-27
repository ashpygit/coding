my_dict={
    'Apple':210, 
    'Orange':300,
    'Papaya':69,
    'Mango':160,
    'Kiwi':290,
    'Grape':80,
    'Blueberry':270,
    'Banana':60,
    'Dragon Fruit':180,
    'Guava':100,
    'Strawberry':70,
    'Other':400
    }

print("My Favorite Fruits Dictionary: ",my_dict,"\n")
print("Print dictionary items: ",my_dict.items(),"\n")

print("Fruits List: ",my_dict.keys(),"\n")
print("Frutis Price: ",my_dict.values(),"\n")

for key,value in my_dict.items():
    print("Price of",key,"--->",value,"per kg")