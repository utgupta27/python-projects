def memo(func):
    memory={}
    def inner(n,m):
        key = str(n)+','+str(m)
        if key not in memory:
            memory[key] = func(n,m)
        return memory[key]
    return inner

@memo
def gtrav(m,n):
    if m == 1 and n == 1 :
        return 1
    if m == 0 or n == 0 :
        return 0
    return gtrav(n-1,m) + gtrav(n,m-1) 

print(gtrav(18,18))
