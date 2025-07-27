def square(a):
    return a*a

result1 = square(4)
print(result1)


#------------Lambda Function below ----------------
f = lambda a : a*a
print(f(5))

f1 = lambda x,y : x+y
print(f1(1,2))



'''
Print a list using lambda44
'''

f = lambda x:'Hello'
print(f(0))

f = lambda :'Lambda with no argument'
print(f())

myfunc = lambda x: range(x)
print(list(myfunc(5)))  