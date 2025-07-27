smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)


if 0 is 0.0:
    print('wow')
else:
    print('oops')

a=9

if a is a:
    print('A wow')
else:
    print('A opps')


message = 'The quick fox i-n the box.org'
msg = message.split()
print(msg)

my_dict = {'Mon':1, 'Tue':2}
print(list(my_dict.items()))

my_dict['Wed'] = 3
my_dict['Thu'] = 4
my_dict['Mon'] = 11

print(my_dict.get('Moon','Key not present'))
print(my_dict.get('Moon'))
print(my_dict.get('Mon'))
print(my_dict)

for i in my_dict:
    print(i)

nums=[1,2,3,4]

print("sorted nums--->",sorted(nums)[1])
print(nums[0:])
print("nums[:2]",nums[:2])



