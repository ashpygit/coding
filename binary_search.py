num_list=[34,6,37,76,223,74,93,39,24,77,65,33,64,16,32,89,88,91]

def binary_search(num):
    sorted_list = sorted(num_list)
    print(sorted_list)
    
    lb = 0
    ub = len(num_list)
    
    for i in range(len(sorted_list)):
        mid = (lb+ub)//2
        if sorted_list[mid] == num:
            print("Number found")
            return True
        else:
            if sorted_list[mid] < num:
                lb = mid+1
            else:
                ub = mid+1
    return False

binary_search(77)