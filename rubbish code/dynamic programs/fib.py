def memo(func):
    memory = {}
    def inner(num):
        if num not in memory:
            memory[num]=func(num)
        return memory[num]
    return inner

@memo
def fib(n):
    if(n<=1):
        return 1
    return fib(n-1)+fib(n-2)
    


# def fibbo(n):
#     if n<=2:
#         return 1
#     elif n>2:
#         c=n-2
#         a=b=1
#         while c>0:
#             temp=b
#             b=a+b
#             a=temp
#             c=c-1
#         return b

print(fib(100))
