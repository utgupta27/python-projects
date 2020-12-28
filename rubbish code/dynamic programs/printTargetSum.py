def memoisation(func):
    memory = {}
    def inner(target,nums):
        key = target
        if key not in memory:
            memory[key] = func(target,nums)
        return memory[key]
    return inner

result =[]
def shortestSum(target,nums):
    if target == 0 : return []
    if target < 0: return None
    for n in nums:
        remainder = target - n
        temp = shortestSum(remainder,nums)
        if temp is not None:
            result.append(n)
        return result

print(shortestSum(20,[3,2,4]))
