nums = [1,5,3,2,9,2]

def sort():
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]


sort()
print(nums)
