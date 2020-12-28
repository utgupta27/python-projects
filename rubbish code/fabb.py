def memo(func):
    cache={}
    def inner(n):
        key = n
        if key not in cache:
            cache[key]=func(n)
        return cache[key]
    return inner

@memo
def fabbo(n):
    if n <= 2: return 1
    return fabbo(n-1)+ fabbo(n-2)

print(fabbo(450))
