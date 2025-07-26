
fibo_list=[]

def fibo(num):
    a = 1
    b = 1

    for i in range(num): 
        a,b = b,a+b
        fibo_list.append(a)
    return 1

fibo(10)
print(fibo_list)
