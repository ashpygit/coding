from functools import reduce

def is_even(n):
    return n%2==0

nums = [1,2,3,4,5,6,7,8,9,10]

print(list(filter(is_even,nums)))

#Using Lambda
even = list(filter(lambda n:n%2==0,nums))
print("Even: ",even)

# Using map function
doubles = list(map(lambda a:a*a,even))
print("Doubles: ",doubles)

# Using reduce function
sum_all = reduce(lambda a,b:a+b, doubles)
print("Sum of all doubles: ",sum_all)