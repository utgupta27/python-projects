def memo(func):
    memory={}
    def inner(num):
        if num not in memory:
            memory[num]=func(num)
        return memory[num]
    return inner

@memo
def facto(n):
    if n==1:
        return 1
    else:
        return n*facto(n-1)

print(facto(20))