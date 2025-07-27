def count_even_odd(lst):
    even = [x for x in list(lst) if x%2==0]
    odd = [y for y in list(lst) if y%2 !=0]
    return len(even),len(odd)

e,o=count_even_odd(list(range(1,11)))
   
print("Count of Even: ",e)
print("Count of Odd: ",o)

#--------------------XXXX-----------------------

name_list = ['Ashish','Anshita','Shivanshu','Mohan','Sohan','Jupiter','Mars','Shani','Golu']

def count_name_len(lst):
    name=[]
    for y in lst:
        x=0
        for z in y:
            x += 1
        if x >5:
            name.append(y)                     
    return name
            
long_name = count_name_len(name_list)
print(long_name)

