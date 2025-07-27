def topten():
    n=1
    while n <= 10:
        sq = n*n
        yield sq #special keyword 
        n+=1
    
a = topten()

for i in a:
    print(i)