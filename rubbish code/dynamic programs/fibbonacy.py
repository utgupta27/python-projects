def memoisation(func):
    cache = {}
    def inner(n):
        key = n
        if key not in cache:
            cache[key] = func(n)
        return cache[key]
    return inner 

@memoisation
def fibbonacy(n):
    if n == 1 or n== 2: return 1
    return fibbonacy(n-1) + fibbonacy(n-2)

print(fibbonacy(400))