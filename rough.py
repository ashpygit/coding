smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest) #op: Smallest:3


if 0 is 0.0:
    print('wow')
else:
    print('oops')  #op: oops

a=9

if a is a:
    print('A wow')
else:
    print('A opps') #op: A Wow


message = 'The quick fox i-n the box.org'
msg = message.split()
print(msg) #op: ['The', 'quick', 'fox', 'i-n', 'the', 'box.org']

my_dict = {'Mon':1, 'Tue':2}
print(list(my_dict.items())) #op: [('Mon', 1), ('Tue', 2)]

my_dict['Wed'] = 3
my_dict['Thu'] = 4
my_dict['Mon'] = 11

print(my_dict.get('Moon','Key not present')) #op: Key not present
print(my_dict.get('Moon')) #op: None
print(my_dict.get('Mon')) #op: 11
print(my_dict) #op: {'Mon': 11, 'Tue': 2, 'Wed': 3, 'Thu': 4}

for i in my_dict:
    print(i)

nums=[1,2,3,4]

print("sorted nums--->",sorted(nums)[1]) #op: sorted nums---> 2
print(nums[0:]) #op: [1,2,3,4]
print("nums[:2]",nums[:2]) #op: [1,2]

for i in range(len(nums)-1,-1,-1):
    print(i,"=",nums[i])

for i in range(len(nums)-1,-1,1):
    print(i,"=",nums[i]) #op: No output

