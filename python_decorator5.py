import time

def count_sum(n):
    j=0
    for i in range(n):
        j=j+i
    print("The sum of the Numbre is ", j)


def count_time(func):
    def wrapper(*args):
        start_time=time.time()
        time.sleep(5)
        func(*args)
        end_time=(time.time()-start_time)/60        
        print(f'The function {func.__name__} took {end_time:.2f} seconds')
    return wrapper

count_time(count_sum)(5)