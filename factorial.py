def facto(x):
    a=1
    b=0
    for i in range(-x,-0):
        b = i*a
        a = b        
    return -b

result = facto(7)
print(result)

import math
print(math.factorial(7))