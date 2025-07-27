def sum_sub(a,b):
    c = a+b
    d = a-b
    print("Sum: ",c)
    print("Sub: ",d)
    
sum_sub(9,5)

#-----------------------------------X-----------------------------------#

def math_val(x,y):
    e = x*y
    f = x**y
    return e,f

g,h = math_val(9,3)
print("Multiply: ",g)
print("Expo: ",h)

#-----------------------------------X-----------------------------------#

def multi_arg(a, *b):
    print("value of b (tuple format): ",b)
    return a+sum(b)

sum_of_all = multi_arg(1,2,3,4,5,6,7,8,9,10)
print("Sum of all number: ",sum_of_all)

#-----------------------------------X-----------------------------------#

def multi_arg(*b):
    print("value of b: ",b)
    return sum(b)

sum_of_all = multi_arg(*range(1,11))
print("Sum of number upto 100: ",sum_of_all)


#-----------------------------------X-----------------------------------#


def kwarg(**data):
    print("This will print data in dictionary format: ",data)
    return data

person_data=kwarg(name='ashish',age='28',place='bangalore',mobile=123456789)
print(person_data)
print(person_data.items())

for k,v in person_data.items():
    print("My",k,"is",v)

#-----------------------------------X-----------------------------------#

def data(*arg, **kwarg):
    print(arg,kwarg)

data(1,2,3,4,'a','b','c',name='xyz')

