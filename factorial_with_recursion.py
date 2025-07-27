def facto_recur(n):

    if n==0:
        return 1
    
    return n * facto_recur(n-1)



result = facto_recur(5)
print(result)