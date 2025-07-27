my_list=[1,2,3,4,5,6,7,8,9,10]

for i in my_list:
    print("value of variable is :", i);

print(my_list[1:5]);

my_list.append("Ashish");

print(my_list);

my_list.append("Mahajan");

print(my_list);


## Numeric List Example
print("************** Numeric List Example *************")
num_list=[]
for i in range(1,11):
    num_list.append(i**2)

print(num_list)

## Slice List Example
print("************** Slice List Example *************")
print(my_list[:3])