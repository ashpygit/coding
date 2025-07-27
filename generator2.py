def callme():
    yield "Hello"

a = callme()
#print(a.__next__()) #op = "Hello"


for i in a:
    print(i)