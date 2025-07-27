def log_function(func):
    def logging(a,b):
        print("calling function: add with argument ",a,b)
        return func(b,-a)
    return logging

#@log_function
def add(a,b):
    return a+b

add = log_function(add)
#print(add) # <function log_function.<locals>.logging at 0x000001AC709994E0>

result = add(2,5)
print(result)