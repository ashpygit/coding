x = 10

def my_func1(a):
    x = a
    print("my_func1 - Local x: ",x)

print("my_func1 - Global x: ",x)

my_func1(15)

#----------------------XX----------------------------

z=100

def my_func2(a):
    global z
    z = a
    print("my_func2 - Local x: ",z)

my_func2(200)
print("my_func2 - Global x: ",z)

#----------------------XX----------------------------


y=1000
print("my_func3 - Global y before func call: ",y)

def my_func3():
    y = 2000
    yy = globals()['y']
    print("my func3 - Global: ",yy)
    print("my_func3 - Local: ",y)

    globals()['y'] = 3000

my_func3()
print("my_func3 - Global y after func call: ",y)




    