import sys

sys.setrecursionlimit(2300)
print(sys.getrecursionlimit())

i = 0
def greet():
    global i
    i += 1
    print("Hello ",i)
    greet()

greet()